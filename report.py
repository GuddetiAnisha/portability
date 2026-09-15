from .analyzer import compatibility_score

def make_report(original, result):
    lines = [
        "# RTL Conversion Report",
        "",
        f"- Source profile: `{result.source_profile}`",
        f"- Target profile: `{result.target_profile}`",
        f"- Detected mapped/vendor constructs: {len(result.findings)}",
        f"- Replacements performed: {result.replacements}",
        f"- Source portability score (heuristic): {compatibility_score(original, result.source_profile)}/100",
        "",
        "## Findings",
    ]
    if result.findings:
        for f in result.findings:
            lines.append(f"- Line {f.line}: **{f.construct}** ({f.category}) — {f.message}")
    else:
        lines.append("- No known profile-specific constructs detected.")

    lines += ["", "## Warnings"]
    if result.warnings:
        lines += [f"- {w}" for w in result.warnings]
    else:
        lines.append("- No unsupported detected constructs in the included educational rule set.")

    lines += [
        "",
        "## Important limitation",
        "This report does not prove functional equivalence, synthesizability, timing closure, or place-and-route success."
    ]
    return "\\n".join(lines)
