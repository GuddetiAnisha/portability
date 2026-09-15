import json
from pathlib import Path

RULE_FILE = Path(__file__).resolve().parents[1] / "mappings" / "primitive_mappings.json"

def load_rules():
    return json.loads(RULE_FILE.read_text(encoding="utf-8"))

def rules_for(source, target):
    data = load_rules()
    return [
        r for r in data["rules"]
        if r["source_profile"] == source and r["target_profile"] == target
    ]
