import re

from models import Finding
from rules import load_rules


def analyze(text: str, source_profile: str):
    data = load_rules()
    findings = []
    known = [
        rule for rule in data["rules"]
        if rule["source_profile"] == source_profile
    ]

    for line_number, line in enumerate(text.splitlines(), 1):
        for rule in known:
            if re.search(rule["detect_regex"], line):
                findings.append(
                    Finding(
                        line=line_number,
                        construct=rule["name"],
                        category=rule["category"],
                        message=f"Detected {rule['name']} for profile {source_profile}",
                    )
                )
    return findings


def compatibility_score(text: str, source_profile: str):
    findings = analyze(text, source_profile)
    penalty = min(80, len(findings) * 10)
    return max(20, 100 - penalty) if findings else 100
