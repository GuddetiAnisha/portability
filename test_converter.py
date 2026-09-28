from analyzer import analyze
from converter import convert


def test_detect_legacy_boolean():
    findings = analyze("enable_cache=yes", "legacy")
    assert any(
        finding.construct == "Legacy boolean yes"
        for finding in findings
    )


def test_legacy_to_standard_boolean():
    result = convert("enable_cache=yes", "legacy", "standard")
    assert "enable_cache=true" in result.converted_text
    assert result.replacements == 1


def test_legacy_timeout_to_standard():
    result = convert("timeout_ms=5000", "legacy", "standard")
    assert "timeout_seconds=5000" in result.converted_text


def test_standard_to_normalized_assignment():
    result = convert("project_name=PlantDoctor", "standard", "normalized")
    assert "project_name: PlantDoctor" in result.converted_text


def test_normalized_to_standard_assignment():
    result = convert("project_name: PlantDoctor", "normalized", "standard")
    assert "project_name=PlantDoctor" in result.converted_text


def test_unknown_text_remains():
    result = convert("custom_setting=something", "legacy", "standard")
    assert "custom_setting=something" in result.converted_text
