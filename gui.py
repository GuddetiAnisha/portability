import difflib

import streamlit as st

from converter import convert
from report import make_report


st.set_page_config(page_title="Software Portability Platform", layout="wide")
st.title("Software Portability & Transformation Platform")
st.caption(
    "Configurable source-pattern analysis, transformation, compatibility scoring, and reporting"
)

source = st.sidebar.selectbox(
    "Source profile",
    ["legacy", "standard", "normalized"],
)
target = st.sidebar.selectbox(
    "Target profile",
    ["standard", "normalized", "legacy"],
)

default = """project_name=PlantDoctor
enable_cache=yes
log_level=DEBUG
timeout_ms=5000
"""

source_text = st.text_area("Source text", default, height=300)

if st.button("Analyze and Transform", type="primary"):
    result = convert(source_text, source, target)
    report = make_report(source_text, result)

    c1, c2 = st.columns(2)
    c1.metric("Detected patterns", len(result.findings))
    c2.metric("Replacements", result.replacements)

    st.subheader("Transformed text")
    st.code(result.converted_text, language="text")

    if result.warnings:
        st.subheader("Warnings")
        for warning in result.warnings:
            st.warning(warning)

    st.subheader("Unified diff")
    diff = "\n".join(
        difflib.unified_diff(
            source_text.splitlines(),
            result.converted_text.splitlines(),
            fromfile="source.txt",
            tofile="transformed.txt",
            lineterm="",
        )
    )
    st.code(diff or "No differences", language="diff")

    st.subheader("Transformation report")
    st.markdown(report)

    st.download_button(
        "Download transformed text",
        result.converted_text,
        "transformed.txt",
    )
    st.download_button(
        "Download report",
        report,
        "transformation_report.md",
    )
