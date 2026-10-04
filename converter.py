import re

from analyzer import analyze
from models import ConversionResult
from rules import rules_for


def convert(text: str, source: str, target: str):
    findings = analyze(text, source)
    transformed = text
    replacements = 0
    warnings = []

    rules = rules_for(source, target)

    for rule in rules:
        # Semantic unit conversion: milliseconds -> seconds.
        # A plain regex replacement would only rename the field and leave
        # the numeric value unchanged (for example 5000 ms -> 5000 s),
        # which is incorrect. Convert the captured value numerically.
        if rule["name"] == "Legacy timeout milliseconds":

            def convert_timeout(match):
                milliseconds = float(match.group(1))
                seconds = milliseconds / 1000
                return f"timeout_seconds={seconds:g}"

            new_text, count = re.subn(
                rule["replace_regex"],
                convert_timeout,
                transformed,
                flags=re.MULTILINE,
            )
        else:
            new_text, count = re.subn(
                rule["replace_regex"],
                rule["replacement"],
                transformed,
                flags=re.MULTILINE,
            )

        if count:
            replacements += count
            transformed = new_text

    detected_names = {finding.construct for finding in findings}
    mapped_names = {rule["name"] for rule in rules}

    for name in sorted(detected_names - mapped_names):
        warnings.append(
            f"No {source}->{target} transformation rule for detected pattern: {name}"
        )

    header = (
        "# Software Portability & Transformation Platform\n"
        f"# Source profile: {source}\n"
        f"# Target profile: {target}\n"
        "# Review transformed output before production use.\n\n"
    )

    return ConversionResult(
        source_profile=source,
        target_profile=target,
        converted_text=header + transformed,
        findings=findings,
        replacements=replacements,
        warnings=warnings,
    )
