#!/usr/bin/env python3
"""
Render DMN decision tables as markdown for the IG.

Reads textualist.dmn and purposive.dmn from input/l2/, parses each
decision table, and appends rendered markdown tables to
input/pagecontent/decision-logic.md (after a marker comment).

Usage:
  python3 render-decision-tables.py
"""

import xml.etree.ElementTree as ET
import os
import html

DMN_NS = "https://www.omg.org/spec/DMN/20191111/MODEL/"
NS = {"dmn": DMN_NS}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
L2_DIR = os.path.join(SCRIPT_DIR, "input", "l2")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "input", "pagecontent", "decision-tables.md")


def parse_dmn(filepath):
    """Parse a DMN file and return a list of decision table dicts."""
    tree = ET.parse(filepath)
    root = tree.getroot()
    decisions = []

    for decision_el in root.findall("dmn:decision", NS):
        decision_id = decision_el.get("id")
        decision_name = decision_el.get("name")

        dt_el = decision_el.find("dmn:decisionTable", NS)
        if dt_el is None:
            continue

        hit_policy = dt_el.get("hitPolicy", "UNIQUE")

        # Parse inputs
        inputs = []
        for inp in dt_el.findall("dmn:input", NS):
            label = inp.get("label", "")
            expr_el = inp.find("dmn:inputExpression", NS)
            type_ref = expr_el.get("typeRef", "") if expr_el is not None else ""
            var_el = expr_el.find("dmn:text", NS) if expr_el is not None else None
            var_name = var_el.text if var_el is not None else ""
            inputs.append({
                "label": label,
                "type": type_ref,
                "variable": var_name,
            })

        # Parse outputs
        outputs = []
        for out in dt_el.findall("dmn:output", NS):
            label = out.get("label", "")
            name = out.get("name", "")
            type_ref = out.get("typeRef", "")
            outputs.append({
                "label": label,
                "name": name,
                "type": type_ref,
            })

        # Parse rules
        rules = []
        for rule_el in dt_el.findall("dmn:rule", NS):
            rule_id = rule_el.get("id", "")
            desc_el = rule_el.find("dmn:description", NS)
            description = desc_el.text.strip() if desc_el is not None and desc_el.text else ""

            input_entries = []
            for ie in rule_el.findall("dmn:inputEntry", NS):
                text_el = ie.find("dmn:text", NS)
                val = text_el.text if text_el is not None and text_el.text else ""
                input_entries.append(val)

            output_entries = []
            for oe in rule_el.findall("dmn:outputEntry", NS):
                text_el = oe.find("dmn:text", NS)
                val = text_el.text if text_el is not None and text_el.text else ""
                output_entries.append(val)

            rules.append({
                "id": rule_id,
                "description": description,
                "inputs": input_entries,
                "outputs": output_entries,
            })

        decisions.append({
            "id": decision_id,
            "name": decision_name,
            "hit_policy": hit_policy,
            "inputs": inputs,
            "outputs": outputs,
            "rules": rules,
        })

    return decisions


def escape_md(text):
    """Escape pipe characters for markdown tables."""
    if not text:
        return "—"
    text = html.unescape(text)
    text = text.replace("|", "\\|")
    # Strip surrounding quotes from string literals for readability
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    if text == "-":
        text = "*(any)*"
    if text == "null":
        text = "*null*"
    return text


def render_decision_table(decision):
    """Render a single decision table as markdown."""
    lines = []

    lines.append(f"**Decision:** {decision['name']}")
    lines.append(f"")
    lines.append(f"**Decision ID:** `{decision['id']}`")
    lines.append(f"")
    lines.append(f"**Hit Policy:** {decision['hit_policy']}")
    lines.append(f"")

    # Build header
    input_headers = [f"**{inp['label']}** ({inp['type']})" for inp in decision["inputs"]]
    output_headers = [f"**{out['label']}** ({out['type']})" for out in decision["outputs"]]
    desc_header = "**Description**"

    headers = ["#"] + input_headers + output_headers + [desc_header]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] * len(headers)) + "|")

    # Build rows
    for i, rule in enumerate(decision["rules"], 1):
        input_cells = [escape_md(v) for v in rule["inputs"]]
        output_cells = [escape_md(v) for v in rule["outputs"]]
        desc_cell = escape_md(rule["description"]) if rule["description"] else "—"

        row = [str(i)] + input_cells + output_cells + [desc_cell]
        lines.append("| " + " | ".join(row) + " |")

    lines.append("")
    return "\n".join(lines)


def render_file(filepath, style_label):
    """Render all decision tables from one DMN file."""
    decisions = parse_dmn(filepath)
    lines = []
    lines.append(f"## {style_label} Decision Tables")
    lines.append("")
    lines.append(f"*Auto-generated from `{os.path.basename(filepath)}` by `render-decision-tables.py`.*")
    lines.append("")

    for decision in decisions:
        lines.append(f"### {decision['name']}")
        lines.append("")
        lines.append(render_decision_table(decision))

    return "\n".join(lines)


def main():
    sections = []

    purposive_path = os.path.join(L2_DIR, "purposive.dmn")
    if os.path.exists(purposive_path):
        sections.append(render_file(purposive_path, "Purposive"))

    textualist_path = os.path.join(L2_DIR, "textualist.dmn")
    if os.path.exists(textualist_path):
        sections.append(render_file(textualist_path, "Textualist"))

    output = "<!-- AUTO-GENERATED by render-decision-tables.py — do not edit by hand -->\n\n"
    output += "This page presents the decision tables from both the purposive and textualist DMN artifacts. "
    output += "The purposive tables encode the interpretive resolutions documented in the "
    output += "[Interpretation Register](register.html). The textualist tables preserve the "
    output += "2021-07 guideline language verbatim. See [Decision Logic](decision-logic.html) "
    output += "for the DRD diagrams and a summary of differences.\n\n"
    output += "\n\n".join(sections)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output)

    print(f"Written {OUTPUT_FILE}")
    print(f"  Purposive: {len(parse_dmn(purposive_path))} decision tables")
    print(f"  Textualist: {len(parse_dmn(textualist_path))} decision tables")


if __name__ == "__main__":
    main()
