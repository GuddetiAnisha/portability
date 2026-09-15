import re
from .models import ConversionResult
from .rules import rules_for
from .analyzer import analyze

def convert(text: str, source: str, target: str):
    findings = analyze(text, source)
    out = text
    replacements = 0
    warnings = []

    rules = rules_for(source, target)
    for rule in rules:
        new_out, count = re.subn(
            rule["replace_regex"],
            rule["replacement"],
            out,
            flags=re.MULTILINE
        )
        if count:
            replacements += count
            out = new_out

    detected_names = {f.construct for f in findings}
    mapped_names = {r["name"] for r in rules}
    unsupported = detected_names - mapped_names
    for name in sorted(unsupported):
        warnings.append(f"No {source}->{target} mapping rule for detected construct: {name}")

    header = (
        f"// RTL Portability Lab conversion\\n"
        f"// Source profile: {source}\\n"
        f"// Target profile: {target}\\n"
        f"// Educational software transformation; verify before synthesis.\\n\\n"
    )
    return ConversionResult(
        source_profile=source,
        target_profile=target,
        converted_text=header + out,
        findings=findings,
        replacements=replacements,
        warnings=warnings,
    )
