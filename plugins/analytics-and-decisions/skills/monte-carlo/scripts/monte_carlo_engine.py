#!/usr/bin/env python3
"""
Monte Carlo Simulation Engine v2
With scenario pathway analysis, devil's advocate failure chains,
and interactive HTML visualization.

Usage:
    python monte_carlo_engine.py <config.json>
    or import and use run_simulation() / generate_html_report() directly
"""

import json
import math
import random
import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Variable:
    """A simulation variable with its distribution parameters."""
    name: str
    distribution: str
    params: dict
    description: str = ""
    devil_advocate_note: str = ""
    failure_chain: str = ""
    recommended_action: str = ""

    def sample(self) -> float:
        d = self.distribution.lower()
        p = self.params

        if d == "fixed":
            return p["value"]
        elif d == "normal":
            return random.gauss(p["mean"], p["std"])
        elif d == "triangular":
            return random.triangular(p["min"], p["max"], p.get("mode", (p["min"] + p["max"]) / 2))
        elif d == "lognormal":
            mean = p["mean"]
            std = p.get("std", mean * 0.3)
            if mean <= 0:
                return 0
            variance = std ** 2
            mu = math.log(mean ** 2 / math.sqrt(variance + mean ** 2))
            sigma = math.sqrt(math.log(1 + variance / mean ** 2))
            return random.lognormvariate(mu, sigma)
        elif d == "beta":
            mean_val = p.get("mean", 0.5)
            sample_size = p.get("sample_size", 100)
            alpha = max(mean_val * sample_size, 0.1)
            beta_param = max((1 - mean_val) * sample_size, 0.1)
            return random.betavariate(alpha, beta_param)
        elif d == "uniform":
            return random.uniform(p["min"], p["max"])
        elif d == "pert":
            a, b, c = p["min"], p.get("mode", (p["min"] + p["max"]) / 2), p["max"]
            if c == a:
                return b
            mu = (a + 4 * b + c) / 6
            alpha_p = 1 + 4 * ((b - a) / (c - a)) if (c - a) > 0 else 2
            beta_p = 1 + 4 * ((c - b) / (c - a)) if (c - a) > 0 else 2
            alpha_p = max(alpha_p, 1.01)
            beta_p = max(beta_p, 1.01)
            sample = random.betavariate(alpha_p, beta_p)
            return a + sample * (c - a)
        elif d == "poisson":
            lam = p.get("lambda", p.get("mean", 5))
            L = math.exp(-lam)
            k = 0
            prob = 1.0
            while prob > L:
                k += 1
                prob *= random.random()
            return k - 1
        else:
            raise ValueError(f"Unknown distribution: {d}")


@dataclass
class ScenarioPathway:
    """A classified scenario zone with narrative and actions."""
    name: str
    color: str
    css_class: str
    range_low: float
    range_high: float
    count: int
    percentage: float
    # These are populated by the caller or LLM — the engine provides the data hooks
    drivers: str = ""
    story: str = ""
    recommended_actions: str = ""
    early_warnings: str = ""
    transitions: str = ""


@dataclass
class SimulationConfig:
    name: str
    description: str
    variables: list
    outcome_formula: str
    outcome_label: str = "Outcome"
    outcome_unit: str = ""
    iterations: int = 10000
    seed: Optional[int] = None
    # Scenario pathway narratives (optional — LLM fills these in)
    scenario_narratives: dict = field(default_factory=dict)
    # Decision matrix (optional — LLM fills these in)
    decision_matrix: list = field(default_factory=list)
    # Risk mitigation strategies (optional — LLM fills these in)
    risk_mitigations: list = field(default_factory=list)
    # Acceleration playbook — how to get to Strong/Exceptional (optional)
    acceleration_playbook: list = field(default_factory=list)


def percentile(data, pct):
    idx = int(pct / 100 * len(data))
    return data[min(idx, len(data) - 1)]


def run_simulation(config: SimulationConfig) -> dict:
    """Run Monte Carlo simulation with scenario pathway analysis."""
    if config.seed is not None:
        random.seed(config.seed)

    results = []
    variable_samples = {v.name: [] for v in config.variables}

    for _ in range(config.iterations):
        sample = {}
        for var in config.variables:
            val = var.sample()
            sample[var.name] = val
            variable_samples[var.name].append(val)

        try:
            outcome = eval(config.outcome_formula, {"__builtins__": {}}, sample)
            results.append(outcome)
        except Exception:
            continue

    if not results:
        return {"error": "No valid simulation results"}

    results.sort()
    n = len(results)
    mean = sum(results) / n
    variance = sum((x - mean) ** 2 for x in results) / n
    std_dev = math.sqrt(variance)

    # Percentile breakpoints
    pcts = {}
    for p in [5, 10, 15, 25, 35, 50, 65, 75, 85, 90, 95]:
        pcts[f"P{p}"] = round(percentile(results, p), 2)

    # Five scenario zones
    zones = [
        ("Catastrophic", "red",    "catastrophic", 0,    10),
        ("Underperform", "orange", "underperform", 10,   35),
        ("Base",         "gray",   "base",         35,   65),
        ("Strong",       "green",  "strong",       65,   90),
        ("Exceptional",  "blue",   "exceptional",  90,   100),
    ]

    scenarios = {}
    for name, color, css, pct_low, pct_high in zones:
        low_val = percentile(results, pct_low) if pct_low > 0 else results[0]
        high_val = percentile(results, pct_high) if pct_high < 100 else results[-1]
        zone_results = [r for r in results if low_val <= r <= high_val]
        count = len(zone_results)

        # Compute which variables are statistically different in this zone vs overall
        zone_indices = [i for i, r in enumerate(results) if low_val <= r <= high_val]
        variable_drivers = {}
        for var in config.variables:
            if var.distribution == "fixed":
                continue
            all_vals = variable_samples[var.name]
            zone_vals = [all_vals[i] for i in zone_indices if i < len(all_vals)]
            if not zone_vals:
                continue
            zone_mean = sum(zone_vals) / len(zone_vals)
            all_mean = sum(all_vals) / len(all_vals)
            all_std = math.sqrt(sum((x - all_mean) ** 2 for x in all_vals) / len(all_vals))
            if all_std > 0:
                z_score = (zone_mean - all_mean) / (all_std / math.sqrt(max(len(zone_vals), 1)))
                variable_drivers[var.name] = {
                    "z_score": round(z_score, 2),
                    "zone_mean": round(zone_mean, 4),
                    "overall_mean": round(all_mean, 4),
                    "significant": abs(z_score) > 1.96,  # p < 0.05
                    "direction": "higher" if z_score > 0 else "lower",
                    "description": var.description,
                }

        # Sort by significance
        sig_drivers = {k: v for k, v in sorted(
            variable_drivers.items(),
            key=lambda x: abs(x[1]["z_score"]),
            reverse=True
        )}

        narratives = config.scenario_narratives.get(css, {})
        scenarios[css] = {
            "name": name,
            "color": color,
            "probability": f"{pct_high - pct_low}%",
            "range": f"{config.outcome_unit}{round(low_val, 0):,.0f} — {config.outcome_unit}{round(high_val, 0):,.0f}",
            "range_low": round(low_val, 2),
            "range_high": round(high_val, 2),
            "count": count,
            "percentage": round(count / n * 100, 1),
            "drivers": sig_drivers,
            "story": narratives.get("story", ""),
            "recommended_actions": narratives.get("recommended_actions", ""),
            "early_warnings": narratives.get("early_warnings", ""),
            "transitions": narratives.get("transitions", ""),
        }

    # Sensitivity analysis
    sensitivity = {}
    for var in config.variables:
        if var.distribution == "fixed":
            continue
        samples = variable_samples[var.name]
        if len(samples) != len(results):
            continue
        var_mean = sum(samples) / len(samples)
        cov = sum((s - var_mean) * (r - mean) for s, r in zip(samples, results)) / n
        var_std = math.sqrt(sum((s - var_mean) ** 2 for s in samples) / n)
        corr = cov / (var_std * std_dev) if (var_std > 0 and std_dev > 0) else 0

        sensitivity[var.name] = {
            "correlation": round(corr, 3),
            "impact": round(abs(corr), 3),
            "direction": "positive" if corr > 0 else "negative",
            "description": var.description,
            "devil_advocate_note": var.devil_advocate_note,
            "failure_chain": var.failure_chain,
            "recommended_action": var.recommended_action,
        }

    sensitivity = dict(sorted(sensitivity.items(), key=lambda x: x[1]["impact"], reverse=True))

    # Histogram
    bucket_count = 50
    range_val = results[-1] - results[0]
    if range_val == 0:
        range_val = 1
    bucket_size = range_val / bucket_count
    histogram = []
    for i in range(bucket_count):
        low = results[0] + i * bucket_size
        high = low + bucket_size
        count = sum(1 for r in results if low <= r < high)
        # Determine zone color
        mid = (low + high) / 2
        if mid < pcts["P10"]:
            clr = "rgba(220, 53, 69, 0.8)"
        elif mid < pcts["P35"]:
            clr = "rgba(255, 165, 0, 0.8)"
        elif mid < pcts["P65"]:
            clr = "rgba(108, 117, 125, 0.8)"
        elif mid < pcts["P90"]:
            clr = "rgba(40, 167, 69, 0.8)"
        else:
            clr = "rgba(59, 130, 246, 0.8)"
        histogram.append({"low": round(low, 2), "high": round(high, 2), "count": count, "color": clr})

    return {
        "name": config.name,
        "description": config.description,
        "outcome_label": config.outcome_label,
        "outcome_unit": config.outcome_unit,
        "iterations": n,
        "mean": round(mean, 2),
        "std_dev": round(std_dev, 2),
        "min": round(results[0], 2),
        "max": round(results[-1], 2),
        "percentiles": pcts,
        "scenarios": scenarios,
        "sensitivity": sensitivity,
        "histogram": histogram,
        "decision_matrix": config.decision_matrix,
        "risk_mitigations": config.risk_mitigations,
        "acceleration_playbook": config.acceleration_playbook,
    }


def generate_html_report(stats: dict, output_path: str):
    """Generate interactive HTML report with scenario pathway cards."""
    p = stats["percentiles"]
    scen = stats["scenarios"]
    sens = stats["sensitivity"]
    hist = stats["histogram"]
    unit = stats.get("outcome_unit", "")
    dm = stats.get("decision_matrix", [])
    risk_mits = stats.get("risk_mitigations", [])
    accel_pb = stats.get("acceleration_playbook", [])

    hist_labels = json.dumps([f"{unit}{h['low']:,.0f}" for h in hist])
    hist_values = json.dumps([h["count"] for h in hist])
    hist_colors = json.dumps([h["color"] for h in hist])

    # Sensitivity data
    sens_names = list(sens.keys())[:8]
    sens_data = [sens[n] for n in sens_names]

    # Zone boundaries for vertical lines
    zone_lines = [
        {"val": p["P10"], "label": "P10", "color": "rgba(220,53,69,0.6)"},
        {"val": p["P35"], "label": "P35", "color": "rgba(255,165,0,0.6)"},
        {"val": p["P65"], "label": "P65", "color": "rgba(108,117,125,0.6)"},
        {"val": p["P90"], "label": "P90", "color": "rgba(40,167,69,0.6)"},
    ]

    # Build scenario pathway cards HTML
    zone_order = ["exceptional", "strong", "base", "underperform", "catastrophic"]
    zone_icons = {
        "exceptional": "&#9733;",  # star
        "strong": "&#9650;",      # up triangle
        "base": "&#9644;",        # rect
        "underperform": "&#9660;", # down triangle
        "catastrophic": "&#9888;", # warning
    }
    zone_colors = {
        "exceptional": "#3b82f6",
        "strong": "#22c55e",
        "base": "#6b7280",
        "underperform": "#f59e0b",
        "catastrophic": "#ef4444",
    }
    zone_bg = {
        "exceptional": "rgba(59,130,246,0.08)",
        "strong": "rgba(34,197,94,0.08)",
        "base": "rgba(107,114,128,0.08)",
        "underperform": "rgba(245,158,11,0.08)",
        "catastrophic": "rgba(239,68,68,0.08)",
    }

    pathway_cards = ""
    for z in zone_order:
        if z not in scen:
            continue
        s = scen[z]
        color = zone_colors[z]
        bg = zone_bg[z]
        icon = zone_icons[z]

        # Build drivers HTML
        drivers_html = ""
        sig_drivers = {k: v for k, v in s.get("drivers", {}).items() if v.get("significant")}
        if sig_drivers:
            for dname, ddata in list(sig_drivers.items())[:3]:
                arrow = "&#8593;" if ddata["direction"] == "higher" else "&#8595;"
                drivers_html += f'<div class="driver-chip" style="border-color:{color}">{arrow} {dname}: {ddata["direction"]} than average (z={ddata["z_score"]})</div>'
        else:
            drivers_html = '<div class="driver-chip" style="border-color:#444">No single variable dominates — driven by combined randomness</div>'

        # Story, actions, warnings
        story_html = f'<p class="pathway-story">{s.get("story", "Narrative will be provided by analysis context.")}</p>' if s.get("story") else ""
        actions_html = f'<div class="pathway-actions"><strong>Recommended Actions:</strong><br>{s.get("recommended_actions", "")}</div>' if s.get("recommended_actions") else ""
        warnings_html = f'<div class="pathway-warnings"><strong>Early Warnings:</strong><br>{s.get("early_warnings", "")}</div>' if s.get("early_warnings") else ""
        transitions_html = f'<div class="pathway-transitions"><strong>Transition Triggers:</strong><br>{s.get("transitions", "")}</div>' if s.get("transitions") else ""

        pathway_cards += f"""
        <div class="pathway-card" style="border-left: 4px solid {color}; background: {bg};">
          <div class="pathway-header">
            <span class="pathway-icon" style="color:{color}">{icon}</span>
            <div>
              <div class="pathway-title" style="color:{color}">{s['name']}</div>
              <div class="pathway-meta">{s['probability']} probability &mdash; {s['range']}</div>
            </div>
          </div>
          <div class="pathway-drivers">{drivers_html}</div>
          {story_html}
          {actions_html}
          {warnings_html}
          {transitions_html}
        </div>"""

    # Build decision matrix HTML
    dm_html = ""
    if dm:
        dm_rows = ""
        for row in dm:
            zc = zone_colors.get(row.get("zone", "base"), "#6b7280")
            dm_rows += f"""<tr>
              <td style="color:{zc};font-weight:600">{row.get('scenario','')}</td>
              <td>{row.get('probability','')}</td>
              <td>{row.get('action','')}</td>
              <td>{row.get('priority','')}</td>
            </tr>"""
        dm_html = f"""
        <div class="card" style="margin-bottom:20px">
          <h2>Decision Matrix</h2>
          <table class="dm-table">
            <thead><tr><th>If Outcome Lands In...</th><th>Probability</th><th>Action</th><th>Priority</th></tr></thead>
            <tbody>{dm_rows}</tbody>
          </table>
        </div>"""

    # Build devil's advocate panel
    devil_items = ""
    for sn in sens_names:
        sd = sens[sn]
        if sd.get("failure_chain") or sd.get("devil_advocate_note"):
            chain = sd.get("failure_chain", "")
            note = sd.get("devil_advocate_note", "")
            action = sd.get("recommended_action", "")
            devil_items += f"""
            <div class="devil-item">
              <div class="devil-var">{sn}</div>
              {'<div class="devil-note">' + note + '</div>' if note else ''}
              {'<div class="devil-chain"><strong>Failure chain:</strong> ' + chain + '</div>' if chain else ''}
              {'<div class="devil-action"><strong>Mitigation:</strong> ' + action + '</div>' if action else ''}
            </div>"""

    # Sensitivity bars
    sens_bars = ""
    for sn in sens_names:
        sd = sens[sn]
        bar_color = "rgba(40,167,69,0.7)" if sd["direction"] == "positive" else "rgba(220,53,69,0.7)"
        width = max(sd["impact"] * 100, 5)
        sens_bars += f"""
        <div class="sens-row">
          <div class="sens-name">{sn}</div>
          <div class="sens-bar-bg"><div class="sens-fill" style="width:{width}%;background:{bar_color}">{sd['impact']:.2f}</div></div>
        </div>"""

    # Pre-build scenario probabilities section (can't nest f-strings)
    scenario_probs_html = ""
    for z in zone_order:
        if z not in scen:
            continue
        zc = zone_colors[z]
        scenario_probs_html += (
            '<div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #21262d">'
            '<div style="display:flex;align-items:center;gap:8px">'
            f'<div style="width:10px;height:10px;border-radius:2px;background:{zc}"></div>'
            f'<span style="color:{zc};font-weight:600;font-size:0.9rem">{scen[z]["name"]}</span>'
            '</div>'
            '<div style="text-align:right">'
            f'<span style="color:#e1e4e8;font-size:0.88rem">{scen[z]["range"]}</span>'
            f'<span style="color:#8b949e;font-size:0.78rem;margin-left:8px">{scen[z]["probability"]}</span>'
            '</div></div>'
        )

    # Pre-build devil panel
    devil_panel_html = ""
    if devil_items:
        devil_panel_html = '<div class="devil-panel"><h2>Devil&#39;s Advocate &mdash; Failure Chains</h2>' + devil_items + '</div>'

    # --- NEW: Risk Mitigation Panel ---
    # Auto-generate from variable data + user-provided mitigations
    risk_mit_html = ""
    risk_items_html = ""

    # Auto-generated from sensitivity analysis: top risk variables
    downside_vars = [
        (name, data) for name, data in sens.items()
        if data.get("failure_chain") or data.get("devil_advocate_note")
    ]
    for idx, (vname, vdata) in enumerate(downside_vars):
        risk_label = vdata.get("description", vname)
        chain = vdata.get("failure_chain", "")
        mitigation = vdata.get("recommended_action", "No specific mitigation defined — identify one before launch.")
        impact_score = vdata.get("impact", 0)
        # Severity color based on sensitivity impact
        if impact_score > 0.5:
            sev_color = "#ef4444"
            sev_label = "HIGH"
        elif impact_score > 0.25:
            sev_color = "#f59e0b"
            sev_label = "MEDIUM"
        else:
            sev_color = "#6b7280"
            sev_label = "LOW"

        chain_html = f'<div class="risk-chain">{chain}</div>' if chain else ""
        risk_items_html += (
            '<div class="risk-item">'
            '<div class="risk-header">'
            f'<span class="risk-severity" style="background:{sev_color}">{sev_label}</span>'
            f'<span class="risk-name">{risk_label}</span>'
            f'<span class="risk-impact">Impact: {impact_score:.2f}</span>'
            '</div>'
            f'{chain_html}'
            f'<div class="risk-mitigation"><span class="risk-shield">&#128737;</span> {mitigation}</div>'
            '</div>'
        )

    # User-provided risk mitigations
    for rm in risk_mits:
        rm_sev_color = rm.get("severity_color", "#f59e0b")
        rm_sev = rm.get("severity", "MEDIUM")
        rm_risk = rm.get("risk", "")
        rm_mit = rm.get("mitigation", "")
        rm_when = rm.get("when_to_act", "")
        rm_when_html = f'<div class="risk-timeline">{rm_when}</div>' if rm_when else ""
        risk_items_html += (
            '<div class="risk-item">'
            '<div class="risk-header">'
            f'<span class="risk-severity" style="background:{rm_sev_color}">{rm_sev}</span>'
            f'<span class="risk-name">{rm_risk}</span>'
            '</div>'
            f'<div class="risk-mitigation"><span class="risk-shield">&#128737;</span> {rm_mit}</div>'
            f'{rm_when_html}'
            '</div>'
        )

    if risk_items_html:
        risk_mit_html = (
            '<div class="risk-panel">'
            '<h2>&#128737; Risk Mitigation Playbook &mdash; How to Avoid the Red &amp; Orange Zones</h2>'
            '<p class="risk-subtitle">Each risk below can push your outcome from Base into Underperform or Catastrophic. '
            'The mitigations are specific actions to take BEFORE the risk materializes.</p>'
            + risk_items_html +
            '</div>'
        )

    # --- NEW: Path to Exceptional Panel ---
    accel_html = ""
    accel_items_html = ""

    # Auto-generated: what drives Strong/Exceptional zones
    upside_drivers = {}
    for zone_key in ["exceptional", "strong"]:
        if zone_key in scen:
            zone_data = scen[zone_key]
            for dname, ddata in zone_data.get("drivers", {}).items():
                if ddata.get("significant") and ddata.get("direction") == "higher":
                    if dname not in upside_drivers or abs(ddata["z_score"]) > abs(upside_drivers[dname]["z_score"]):
                        upside_drivers[dname] = ddata
                        upside_drivers[dname]["source_zone"] = zone_key

    if upside_drivers:
        accel_items_html += '<div class="accel-drivers"><h3>Variables That Drive Exceptional Outcomes</h3>'
        for dname, ddata in sorted(upside_drivers.items(), key=lambda x: abs(x[1]["z_score"]), reverse=True):
            zone_label = "Exceptional" if ddata.get("source_zone") == "exceptional" else "Strong"
            # Find the matching variable to get its recommended_action
            var_action = ""
            for sn, sd in sens.items():
                if sn == dname:
                    var_action = sd.get("recommended_action", "")
                    break
            action_html = f'<div class="accel-driver-action">Lever: {var_action}</div>' if var_action else ""
            accel_items_html += (
                '<div class="accel-driver">'
                f'<div class="accel-driver-name">&#9650; {dname}</div>'
                f'<div class="accel-driver-detail">In {zone_label} scenarios, this variable was significantly higher than average (z={ddata["z_score"]})</div>'
                f'{action_html}'
                '</div>'
            )
        accel_items_html += '</div>'

    # Also show what's significantly LOWER in Catastrophic/Underperform (things to avoid)
    downside_drivers = {}
    for zone_key in ["catastrophic", "underperform"]:
        if zone_key in scen:
            zone_data = scen[zone_key]
            for dname, ddata in zone_data.get("drivers", {}).items():
                if ddata.get("significant") and ddata.get("direction") == "lower":
                    if dname not in downside_drivers or abs(ddata["z_score"]) > abs(downside_drivers[dname]["z_score"]):
                        downside_drivers[dname] = ddata

    if downside_drivers:
        accel_items_html += '<div class="accel-avoid"><h3>Variables That Drag You Down</h3>'
        for dname, ddata in sorted(downside_drivers.items(), key=lambda x: abs(x[1]["z_score"]), reverse=True):
            accel_items_html += (
                '<div class="accel-driver" style="border-left-color:#ef4444">'
                f'<div class="accel-driver-name" style="color:#ef4444">&#9660; {dname}</div>'
                f'<div class="accel-driver-detail">In bad scenarios, this variable was significantly lower than average (z={ddata["z_score"]})</div>'
                '</div>'
            )
        accel_items_html += '</div>'

    # User-provided acceleration playbook steps
    if accel_pb:
        accel_items_html += '<div class="accel-plays"><h3>Acceleration Playbook &mdash; Your Moves</h3>'
        for idx, play in enumerate(accel_pb):
            phase_label = play.get("phase", f"Step {idx+1}")
            play_action = play.get("action", "")
            play_target = play.get("target", "")
            play_measure = play.get("measure", "")
            target_html = f'<div class="accel-play-target">Target: {play_target}</div>' if play_target else ""
            measure_html = f'<div class="accel-play-metric">Measure: {play_measure}</div>' if play_measure else ""
            accel_items_html += (
                '<div class="accel-play">'
                f'<div class="accel-play-phase">{phase_label}</div>'
                f'<div class="accel-play-action">{play_action}</div>'
                f'{target_html}'
                f'{measure_html}'
                '</div>'
            )
        accel_items_html += '</div>'

    if accel_items_html:
        accel_html = (
            '<div class="accel-panel">'
            '<h2>&#9733; Path to Exceptional &mdash; How to Shift the Distribution Up</h2>'
            '<p class="accel-subtitle">The simulation reveals which variables drive the best outcomes. '
            'These are your highest-leverage moves to shift from Base toward Strong and Exceptional.</p>'
            + accel_items_html +
            '</div>'
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Monte Carlo: {stats['name']}</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:system-ui,sans-serif;background:#0f1117;color:#e1e4e8;padding:24px;line-height:1.6}}
.container{{max-width:1200px;margin:0 auto}}
h1{{font-size:1.8rem;color:#fff;margin-bottom:4px}}
.subtitle{{color:#8b949e;margin-bottom:28px;font-size:0.9rem}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;margin-bottom:24px}}
.card{{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:24px}}
.card h2{{font-size:1rem;color:#c9d1d9;margin-bottom:14px;border-bottom:1px solid #30363d;padding-bottom:8px}}
.planning-number{{font-size:3.2rem;font-weight:700;color:#58a6ff;text-align:center;padding:16px 0 4px}}
.planning-label{{text-align:center;color:#8b949e;font-size:0.82rem;margin-bottom:12px}}
.pct-row{{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #21262d;font-size:0.88rem}}
.pct-row:last-child{{border-bottom:none}}
.pct-label{{color:#8b949e}}
.pct-value{{font-weight:600;font-variant-numeric:tabular-nums}}
.chart-box{{position:relative;height:280px}}
.pathway-section{{margin-bottom:24px}}
.pathway-section h2{{font-size:1.15rem;color:#c9d1d9;margin-bottom:16px}}
.pathway-card{{border-radius:10px;padding:20px;margin-bottom:12px;transition:all 0.2s}}
.pathway-card:hover{{transform:translateX(4px)}}
.pathway-header{{display:flex;align-items:center;gap:12px;margin-bottom:12px}}
.pathway-icon{{font-size:1.5rem}}
.pathway-title{{font-size:1.05rem;font-weight:700}}
.pathway-meta{{font-size:0.8rem;color:#8b949e}}
.pathway-drivers{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}}
.driver-chip{{font-size:0.78rem;padding:4px 10px;border:1px solid;border-radius:20px;color:#c9d1d9;background:rgba(255,255,255,0.03)}}
.pathway-story{{color:#c9d1d9;font-size:0.88rem;margin-bottom:8px;font-style:italic}}
.pathway-actions,.pathway-warnings,.pathway-transitions{{font-size:0.82rem;color:#8b949e;margin-top:6px;padding:8px 12px;background:rgba(0,0,0,0.2);border-radius:6px}}
.pathway-actions strong,.pathway-warnings strong,.pathway-transitions strong{{color:#c9d1d9}}
.sens-row{{display:flex;align-items:center;padding:5px 0}}
.sens-name{{width:180px;font-size:0.82rem;color:#c9d1d9;text-align:right;padding-right:12px;flex-shrink:0}}
.sens-bar-bg{{flex:1;height:22px;background:#21262d;border-radius:4px;overflow:hidden}}
.sens-fill{{height:100%;border-radius:4px;display:flex;align-items:center;padding-left:8px;font-size:0.72rem;color:#fff;min-width:30px}}
.devil-panel{{background:#1c1208;border:1px solid #5a3e0a;border-radius:12px;padding:24px;margin-bottom:24px}}
.devil-panel h2{{color:#f0ad4e;border-bottom-color:#5a3e0a}}
.devil-item{{padding:10px 0;border-bottom:1px solid #2a1f08}}
.devil-item:last-child{{border-bottom:none}}
.devil-var{{font-weight:600;color:#f0ad4e;font-size:0.92rem}}
.devil-note{{color:#c9a54e;font-size:0.84rem;margin-top:4px}}
.devil-chain{{color:#d4a853;font-size:0.82rem;margin-top:6px;padding:8px;background:rgba(0,0,0,0.25);border-radius:4px;border-left:2px solid #f0ad4e}}
.devil-action{{color:#7cb87c;font-size:0.82rem;margin-top:4px;padding:8px;background:rgba(0,60,0,0.15);border-radius:4px;border-left:2px solid #28a745}}
.risk-panel{{background:#1a0c0c;border:1px solid #5a1a1a;border-radius:12px;padding:24px;margin-bottom:24px}}
.risk-panel h2{{color:#ef4444;border-bottom:1px solid #5a1a1a;padding-bottom:8px;margin-bottom:6px}}
.risk-subtitle{{color:#8b949e;font-size:0.82rem;margin-bottom:16px}}
.risk-item{{padding:14px 0;border-bottom:1px solid #2a0f0f}}
.risk-item:last-child{{border-bottom:none}}
.risk-header{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}
.risk-severity{{font-size:0.68rem;font-weight:700;padding:2px 8px;border-radius:3px;color:#fff;letter-spacing:0.5px}}
.risk-name{{font-weight:600;color:#e1e4e8;font-size:0.9rem}}
.risk-impact{{color:#8b949e;font-size:0.78rem;margin-left:auto}}
.risk-chain{{color:#d4a853;font-size:0.82rem;margin:6px 0;padding:8px;background:rgba(0,0,0,0.25);border-radius:4px;border-left:2px solid #f59e0b}}
.risk-mitigation{{color:#7cb87c;font-size:0.85rem;margin-top:6px;padding:10px;background:rgba(0,60,0,0.15);border-radius:6px;border-left:3px solid #28a745}}
.risk-shield{{margin-right:4px}}
.risk-timeline{{color:#8b949e;font-size:0.78rem;margin-top:4px;padding-left:14px;font-style:italic}}
.accel-panel{{background:#0c1a0c;border:1px solid #1a5a1a;border-radius:12px;padding:24px;margin-bottom:24px}}
.accel-panel h2{{color:#22c55e;border-bottom:1px solid #1a5a1a;padding-bottom:8px;margin-bottom:6px}}
.accel-subtitle{{color:#8b949e;font-size:0.82rem;margin-bottom:16px}}
.accel-drivers,.accel-avoid,.accel-plays{{margin-bottom:16px}}
.accel-drivers h3,.accel-avoid h3,.accel-plays h3{{color:#c9d1d9;font-size:0.92rem;margin-bottom:10px}}
.accel-driver{{padding:10px 12px;margin-bottom:8px;background:rgba(34,197,94,0.06);border-left:3px solid #22c55e;border-radius:4px}}
.accel-driver-name{{font-weight:600;color:#22c55e;font-size:0.9rem}}
.accel-driver-detail{{color:#8b949e;font-size:0.82rem;margin-top:4px}}
.accel-driver-action{{color:#7cb87c;font-size:0.84rem;margin-top:6px;padding:6px 8px;background:rgba(0,60,0,0.2);border-radius:4px}}
.accel-play{{padding:12px;margin-bottom:8px;background:rgba(59,130,246,0.06);border-left:3px solid #3b82f6;border-radius:4px}}
.accel-play-phase{{font-weight:700;color:#3b82f6;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.5px}}
.accel-play-action{{color:#e1e4e8;font-size:0.88rem;margin-top:4px}}
.accel-play-target,.accel-play-metric{{color:#8b949e;font-size:0.78rem;margin-top:4px}}
.dm-table{{width:100%;border-collapse:collapse;font-size:0.85rem}}
.dm-table th{{text-align:left;padding:8px;border-bottom:2px solid #30363d;color:#8b949e;font-weight:500}}
.dm-table td{{padding:8px;border-bottom:1px solid #21262d}}
.meta{{text-align:center;color:#484f58;font-size:0.72rem;margin-top:28px}}
.legend{{display:flex;gap:16px;justify-content:center;margin-bottom:20px;flex-wrap:wrap}}
.legend-item{{display:flex;align-items:center;gap:6px;font-size:0.78rem;color:#8b949e}}
.legend-dot{{width:12px;height:12px;border-radius:3px}}
</style>
</head>
<body>
<div class="container">
  <h1>{stats['name']}</h1>
  <p class="subtitle">{stats['description']} &mdash; {stats['iterations']:,} simulations</p>

  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:#ef4444"></div>Catastrophic (&lt;P10)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#f59e0b"></div>Underperform (P10-P35)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#6b7280"></div>Base (P35-P65)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#22c55e"></div>Strong (P65-P90)</div>
    <div class="legend-item"><div class="legend-dot" style="background:#3b82f6"></div>Exceptional (P90+)</div>
  </div>

  <div class="grid">
    <div class="card">
      <h2>Planning Number (P50)</h2>
      <div class="planning-number">{unit}{p['P50']:,.0f}</div>
      <div class="planning-label">Median outcome &mdash; resource against this</div>
      <div class="pct-row"><span class="pct-label">P90 (optimistic)</span><span class="pct-value" style="color:#3b82f6">{unit}{p['P90']:,.0f}</span></div>
      <div class="pct-row"><span class="pct-label">P75</span><span class="pct-value" style="color:#22c55e">{unit}{p['P75']:,.0f}</span></div>
      <div class="pct-row"><span class="pct-label">P50 (plan here)</span><span class="pct-value" style="color:#58a6ff">{unit}{p['P50']:,.0f}</span></div>
      <div class="pct-row"><span class="pct-label">P25</span><span class="pct-value" style="color:#f59e0b">{unit}{p['P25']:,.0f}</span></div>
      <div class="pct-row"><span class="pct-label">P10 (pessimistic)</span><span class="pct-value" style="color:#ef4444">{unit}{p['P10']:,.0f}</span></div>
    </div>
    <div class="card">
      <h2>Scenario Probabilities</h2>
      {scenario_probs_html}
    </div>
  </div>

  <!-- Distribution Histogram -->
  <div class="card" style="margin-bottom:20px">
    <h2>Outcome Distribution</h2>
    <div class="chart-box"><canvas id="histChart"></canvas></div>
  </div>

  <!-- Scenario Pathway Cards -->
  <div class="pathway-section">
    <h2 style="padding-left:4px">Scenario Pathways &mdash; What Drives Each Future</h2>
    {pathway_cards}
  </div>

  <!-- Sensitivity Analysis -->
  <div class="card" style="margin-bottom:20px">
    <h2>Sensitivity Analysis &mdash; What Matters Most</h2>
    {sens_bars}
  </div>

  <!-- Devil's Advocate -->
  {devil_panel_html}

  <!-- Risk Mitigation Playbook -->
  {risk_mit_html}

  <!-- Path to Exceptional -->
  {accel_html}

  <!-- Decision Matrix -->
  {dm_html}

  <p class="meta">Monte Carlo Analysis &mdash; Scenario Pathway Engine v2</p>
</div>

<script>
const ctx = document.getElementById('histChart').getContext('2d');
new Chart(ctx, {{
  type: 'bar',
  data: {{
    labels: {hist_labels},
    datasets: [{{
      data: {hist_values},
      backgroundColor: {hist_colors},
      borderWidth: 0,
      borderRadius: 2,
      barPercentage: 1.0,
      categoryPercentage: 1.0,
    }}]
  }},
  options: {{
    responsive: true,
    maintainAspectRatio: false,
    plugins: {{
      legend: {{ display: false }},
      tooltip: {{
        callbacks: {{
          title: (items) => {{
            const i = items[0].dataIndex;
            const labels = {hist_labels};
            return labels[i];
          }},
          label: (item) => item.raw + ' simulations'
        }}
      }}
    }},
    scales: {{
      x: {{ display: false }},
      y: {{ grid: {{ color: '#21262d' }}, ticks: {{ color: '#8b949e', font: {{ size: 11 }} }} }}
    }}
  }}
}});
</script>
</body>
</html>"""

    with open(output_path, "w") as f:
        f.write(html)
    return output_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
        with open(config_path) as f:
            config_data = json.load(f)

        variables = [Variable(**v) for v in config_data["variables"]]
        config = SimulationConfig(
            name=config_data["name"],
            description=config_data.get("description", ""),
            variables=variables,
            outcome_formula=config_data["outcome_formula"],
            outcome_label=config_data.get("outcome_label", "Outcome"),
            outcome_unit=config_data.get("outcome_unit", ""),
            iterations=config_data.get("iterations", 10000),
            seed=config_data.get("seed"),
            scenario_narratives=config_data.get("scenario_narratives", {}),
            decision_matrix=config_data.get("decision_matrix", []),
            risk_mitigations=config_data.get("risk_mitigations", []),
            acceleration_playbook=config_data.get("acceleration_playbook", []),
        )

        results = run_simulation(config)
        output_path = config_data.get("output_path", "/tmp/monte_carlo_report.html")
        generate_html_report(results, output_path)
        print(json.dumps(results, indent=2, default=str))
    else:
        print("Usage: python monte_carlo_engine.py <config.json>")
