#!/usr/bin/env bash
# validate.sh — bash-only sanity checks for the skill graph.
# Runs Checks 1 (orphans), 2 (dead INDEX links), 4 (and-in-core), 7 (expired overlays),
# 9 (sub-folders), and the mode-gated Checks 10-11 (org-admin) and 12 (org-member).
# Checks 3, 5, 6, and 8 need judgment and run only in the graph-validate skill.
# Exits 0 on PASS, 1 on any violation.
#
# Usage:  ./tools/validate.sh [ROOT]
# Example: ./tools/validate.sh .

set -u
ROOT="${1:-.}"
cd "$ROOT" || { echo "Cannot cd to $ROOT"; exit 2; }

fail=0
say()     { printf "  - %s\n" "$1"; }
section() { printf "\n[%s] %s\n" "$1" "$2"; }

# --- Check 1: every skill file is listed in skills/INDEX.md ----------------
section "Check 1" "Orphan nodes (files not in skills/INDEX.md)"
if [ -f skills/INDEX.md ]; then
  while IFS= read -r f; do
    base="${f#./}"
    # match either bare name or full path inside [[...]]
    name="$(basename "$f" .md)"
    if ! grep -qE "\[\[(skills/[^]]+/)?${name}\]\]" skills/INDEX.md; then
      say "ORPHAN: $base"
      fail=1
    fi
  done < <(find ./skills/core ./skills/workflows ./skills/domains ./skills/context -type f -name '*.md' 2>/dev/null)
else
  say "skills/INDEX.md missing"
  fail=1
fi

# --- Check 2: every wikilink in INDEX resolves to a real file --------------
section "Check 2" "Dead links in skills/INDEX.md"
if [ -f skills/INDEX.md ]; then
  while IFS= read -r link; do
    # strip [[ and ]]
    inner="${link#\[\[}"
    inner="${inner%\]\]}"
    # only check skill-graph links
    case "$inner" in
      skills/*)
        path="${inner}.md"
        if [ ! -f "$path" ]; then
          say "DEAD: [[$inner]] — no file at $path"
          fail=1
        fi
        ;;
    esac
  done < <(grep -oE '\[\[[^]]+\]\]' skills/INDEX.md | sort -u)
fi

# --- Check 4: no " and " in core skill descriptions ------------------------
section "Check 4" "Core skills with 'and' in their description (two jobs in one)"
if [ -d skills/core ]; then
  while IFS= read -r f; do
    line="$(grep -E '^description:' "$f" | head -1)"
    if printf '%s' "$line" | grep -qiE ' and '; then
      say "TWO-JOB: $f — $line"
      fail=1
    fi
  done < <(find ./skills/core -type f -name '*.md')
fi

# --- Detect mode ----------------------------------------------------------
mode="individual"
if [ -f MODE.md ]; then
  m="$(grep -E '^mode:' MODE.md | head -1 | awk '{print $2}')"
  [ -n "$m" ] && mode="$m"
fi
printf "\nMode: %s\n" "$mode"

# --- Check 10: stewardship on org domains (org-admin mode only) -----------
if [ "$mode" = "org-admin" ]; then
  section "Check 10" "Org-level domains without a steward"
  if [ -d skills/domains ]; then
    while IFS= read -r f; do
      scope="$(grep -E '^scope:' "$f" | head -1 | awk '{print $2}')"
      if [ "$scope" = "org" ]; then
        stew="$(grep -E '^steward:' "$f" | head -1 | awk '{print $2}')"
        if [ -z "$stew" ] || [ "$stew" = "<name" ] || [ "$stew" = "null" ]; then
          say "NO_STEWARD: $f — set steward: <human name>"
          fail=1
        fi
      fi
    done < <(find ./skills/domains -type f -name '*.md')
  fi

  # --- Check 11: fork policy on org workflows -----------------------------
  section "Check 11" "Org-level workflows without fork policy"
  if [ -d skills/workflows ]; then
    while IFS= read -r f; do
      scope="$(grep -E '^scope:' "$f" | head -1 | awk '{print $2}')"
      if [ "$scope" = "org" ]; then
        if ! grep -qE '^personal_fork_allowed:\s*(true|false)' "$f"; then
          say "NO_FORK_POLICY: $f — set personal_fork_allowed: true|false"
          fail=1
        fi
      fi
    done < <(find ./skills/workflows -type f -name '*.md')
  fi
fi

# --- Check 12: fork lineage on personal workflows (org-member mode) -------
if [ "$mode" = "org-member" ]; then
  section "Check 12" "Personal workflows without fork lineage"
  org_ws="$(grep -E '^org_workspace:' MODE.md | head -1 | awk '{print $2}')"
  if [ -n "$org_ws" ] && [ -d "$org_ws/skills/workflows" ]; then
    while IFS= read -r f; do
      base="$(basename "$f")"
      if [ -f "$org_ws/skills/workflows/$base" ]; then
        if ! grep -qE '^forks:' "$f"; then
          say "NO_LINEAGE: $f shadows org workflow $base — add forks: $base"
          fail=1
        fi
      fi
    done < <(find ./skills/workflows -type f -name '*.md')
  fi
fi

# --- Check 9: flat-folder discipline (no sub-folders) ---------------------
section "Check 9" "Sub-folders inside skills/ (hierarchy sneaking back in)"
for top in core workflows domains context; do
  if [ -d "skills/$top" ]; then
    while IFS= read -r d; do
      [ -z "$d" ] && continue
      say "SUBFOLDER: skills/$top/$(basename "$d") — flatten or extract via graph-grow"
      fail=1
    done < <(find "skills/$top" -mindepth 1 -type d 2>/dev/null)
  fi
done

# --- Check 7: expired context overlays still in skills/context -------------
section "Check 7" "Expired context overlays"
today="$(date +%Y-%m-%d)"
if [ -d skills/context ]; then
  while IFS= read -r f; do
    exp="$(grep -E '^expires:' "$f" | head -1 | awk '{print $2}')"
    if [ -n "$exp" ] && [ "$exp" != "on-completion" ]; then
      if [ "$exp" \< "$today" ]; then
        say "EXPIRED: $f (expired $exp)"
        fail=1
      fi
    fi
  done < <(find ./skills/context -type f -name '*.md')
fi

# --- Summary ---------------------------------------------------------------
printf "\n"
if [ "$fail" -eq 0 ]; then
  echo "PASS — graph integrity checks ok."
else
  echo "FAIL — fix the items above. Use /graph-grow in your agent to make structural changes."
fi
exit "$fail"
