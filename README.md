# Software Portability & Transformation Platform

A Python software project for analysing structured text, detecting configurable source patterns, applying rule-based transformations, and generating compatibility reports.

The repository is software-only and focuses on parsing, transformation rules, reporting, testing, and an interactive Streamlit interface.

## Features

- Configurable pattern detection
- JSON-based transformation rules
- Source-to-source text transformation
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

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    python main.py sample_legacy.txt --source legacy --target standard --output converted.txt

Run the GUI with:

    streamlit run gui.py

Run tests with:

    pytest -q

## Software focus

This project demonstrates Python automation, regular-expression based pattern analysis, structured JSON configuration, transformation pipelines, compatibility analysis, automated reporting, Streamlit interfaces, and reproducible testing.

## Scope

The repository does not contain RTL, SystemVerilog, FPGA/ASIC logic, hardware mapping, synthesis flows, or hardware-specific examples.
