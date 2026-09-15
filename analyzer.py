import re
from .models import Finding
from .rules import load_rules

def analyze(text: str, source_profile: str):
    data = load_rules()
    findings = []
    known = [r for r in data["rules"] if r["source_profile"] == source_profile]
    for i, line in enumerate(text.splitlines(), 1):
        for rule in known:
            if re.search(rule["detect_regex"], line):
                findings.append(Finding(
                    line=i,
                    construct=rule["name"],
                    category=rule["category"],
                    message=f"Detected {rule['name']} for profile {source_profile}"
                ))
    return findings

def compatibility_score(text: str, source_profile: str):
    findings = analyze(text, source_profile)
    penalty = min(80, len(findings) * 12)
    return max(20, 100 - penalty)
