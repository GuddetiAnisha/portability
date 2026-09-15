# RTL Portability Lab

A software-only Python prototype inspired by the general RTL portability problem in Ericsson Req ID 790480, but intentionally adapted into an independent project.

## Changed scope

Instead of promising a full ASIC↔FPGA implementation flow or place-and-route closure, this project focuses on the software engineering side:

- parse and inspect Verilog/SystemVerilog source
- detect vendor-specific primitives/IP patterns
- convert recognized constructs through configurable mapping rules
- target a portable generic RTL abstraction or another vendor profile
- generate conversion reports and compatibility warnings
- compare source/target constructs
- provide a simple Streamlit GUI
- verify transformations with automated tests

It does **not** claim synthesis, place-and-route, timing closure, or physical FPGA/ASIC validation.

## Profiles

- generic
- xilinx
- intel
- asic_generic

The included rules are educational examples, not production vendor libraries.

## Features

- Python conversion engine
- Regex/token-aware rule matching for a constrained subset
- JSON mapping database
- Primitive/IP detection
- Direction-aware conversion
- Compatibility scoring
- Unsupported-construct warnings
- Diff preview
- CLI
- Streamlit GUI
- Conversion report
- Pytest tests

## Install

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
```

## GUI

```bash
streamlit run gui.py
```

## CLI

```bash
python main.py rtl_samples/xilinx_example.sv --source xilinx --target generic --output converted.sv
```

## Tests

```bash
pytest -q
```

## Good future extensions

- tree-sitter/SystemVerilog AST parser
- Yosys integration for syntax/elaboration checks
- richer primitive libraries
- equivalence checking
- vendor-tool adapters when licensed EDA tools are available
- React/TypeScript GUI
