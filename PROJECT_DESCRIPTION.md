# RTL Portability Lab — Project Description

## Goal

Explore how software can improve RTL portability across implementation targets by detecting vendor-specific constructs and applying configurable transformation rules.

## Deliberate changes from the thesis description

This is not a reproduction of Ericsson's internal thesis work. The prototype:

- uses an independent educational mapping database;
- focuses on static RTL analysis and source-to-source transformation;
- introduces a neutral `generic` portability profile;
- adds compatibility scoring, diff inspection, warnings, and reports;
- uses a Streamlit GUI rather than vendor EDA GUIs;
- does not perform synthesis, implementation, place-and-route, timing closure, or hardware validation.

## Software architecture

RTL input → profile analyzer → primitive/IP detector → mapping-rule engine → converted RTL → compatibility/reporting layer → GUI/CLI.

## Technologies

Python, regular expressions for a constrained educational RTL subset, JSON mapping rules, Streamlit, Pytest.

## Important engineering limitation

Regex transformations are intentionally limited. A production-grade implementation should use a real Verilog/SystemVerilog parser or AST and formal/equivalence verification.
