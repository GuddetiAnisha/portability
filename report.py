from analyzer import compatibility_score


def make_report(original, result):
    lines = [
        "# Transformation Report",
        "",
        f"- Source profile: {result.source_profile}",
        f"- Target profile: {result.target_profile}",
        f"- Detected source patterns: {len(result.findings)}",
        f"- Replacements performed: {result.replacements}",
        f"- Source compatibility score (heuristic): {compatibility_score(original, result.source_profile)}/100",
        "",
        "## Findings",
    ]

    if result.findings:
        for finding in result.findings:
            lines.append(
                f"- Line {finding.line}: {finding.construct} "
                f"({finding.category}) - {finding.message}"
            )
    else:
        lines.append("- No known profile-specific patterns detected.")

    lines += ["", "## Warnings"]

    if result.warnings:
        lines += [f"- {warning}" for warning in result.warnings]
    else:
        lines.append("- No unsupported detected patterns in the current rule set.")

    lines += [
        "",
        "## Important limitation",
        (
            "This report is based on configurable pattern rules. "
            "It does not prove semantic equivalence for arbitrary "
            "programming languages or configuration formats."
        ),
    ]

    return "\n".join(lines)
