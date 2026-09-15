from dataclasses import dataclass, field

@dataclass
class Finding:
    line: int
    construct: str
    category: str
    message: str

@dataclass
class ConversionResult:
    source_profile: str
    target_profile: str
    converted_text: str
    findings: list[Finding] = field(default_factory=list)
    replacements: int = 0
    warnings: list[str] = field(default_factory=list)
