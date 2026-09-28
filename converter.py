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
        f"# Software Portability & Transformation Platform\n"
        f"# Source profile: {source}\n"
        f"# Target profile: {target}\n"
        f"# Review transformed output before production use.\n\n"
    )

    return ConversionResult(
        source_profile=source,
        target_profile=target,
        converted_text=header + transformed,
        findings=findings,
        replacements=replacements,
        warnings=warnings,
    )
