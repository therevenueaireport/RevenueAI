---
type: kit-config
required: true
always_loaded: true
---

# MODE.md

```yaml
mode: individual    # one of: individual | org-admin | org-member
```

### individual (default)
Solo user. Single source of truth = you. No stewards, no fork rights.

### org-admin
Deploying at org level. Every domain needs a steward. Every workflow declares fork policy.

### org-member
Joining an existing org instance. Read CORE / WORKFLOWS / DOMAINS from the org workspace.

```yaml
org_workspace: <path-or-url-to-org-kit>    # required only when mode is org-member
```

See the governance guide in the graph-concept skill for the full operating manual.
