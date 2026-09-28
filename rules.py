import json
from pathlib import Path


RULE_FILE = Path(__file__).resolve().parent / "transformation_rules.json"


def load_rules():
    return json.loads(RULE_FILE.read_text(encoding="utf-8"))


def rules_for(source, target):
    data = load_rules()
    return [
        rule
        for rule in data["rules"]
        if rule["source_profile"] == source
        and rule["target_profile"] == target
    ]
