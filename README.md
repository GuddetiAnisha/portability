# Software Portability & Transformation Platform

A Python software project for analysing structured text, detecting configurable source patterns, applying rule-based transformations, and generating compatibility reports.

The repository is software-only and focuses on parsing, transformation rules, reporting, testing, and an interactive Streamlit interface.

## Features

- Configurable pattern detection
- JSON-based transformation rules
- Source-to-source text transformation
- Semantic milliseconds-to-seconds timeout conversion
- Compatibility scoring
- Unsupported-pattern warnings
- Source-versus-transformed diff inspection
- Command-line interface
- Streamlit dashboard
- Markdown report generation
- Automated Pytest validation

## Profiles

The demo rules use three generic software profiles: legacy, standard, and normalized.

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py sample_legacy.txt --source legacy --target standard --output converted.txt
```

Run the GUI with:

```powershell
python -m streamlit run gui.py
```

Run tests with:

```powershell
python -m pytest -q
```

## Verified transformation behavior

Local validation identified and fixed a semantic unit-conversion bug. Previously, the timeout rule renamed the field without converting its numeric value:

```text
timeout_ms=5000 -> timeout_seconds=5000
```

The converter now performs the correct unit conversion:

```text
timeout_ms=5000 -> timeout_seconds=5
timeout_ms=2500 -> timeout_seconds=2.5
```

Boolean normalization was also verified:

```text
enable_cache=yes -> enable_cache=true
```

The Streamlit workflow was checked with a legacy profile and standard target profile. The interface correctly displayed detected patterns, replacement count, transformed text, unified diff, and transformation report.

See `RESULTS.md` for the validation summary and the discovered/fixed issue.

## Software focus

This project demonstrates Python automation, regular-expression based pattern analysis, structured JSON configuration, transformation pipelines, compatibility analysis, automated reporting, Streamlit interfaces, and reproducible testing.

## Scope

This is a controlled rule-based transformation prototype. Regex-driven transformations are suitable for known structured text formats, but transformed output should still be reviewed before production use.

The repository does not contain RTL, SystemVerilog, FPGA/ASIC logic, hardware mapping, synthesis flows, or hardware-specific examples.
