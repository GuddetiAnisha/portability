import difflib
import streamlit as st
from app.converter import convert
from app.report import make_report

st.set_page_config(page_title="RTL Portability Lab", layout="wide")
st.title("RTL Portability Lab")
st.caption("Software-only vendor-aware RTL conversion and compatibility explorer")

source = st.sidebar.selectbox("Source profile", ["xilinx", "intel", "asic_generic", "generic"])
target = st.sidebar.selectbox("Target profile", ["generic", "xilinx", "intel", "asic_generic"])

default = """module demo(input wire i, output wire o);
  BUFG u_clk (.I(i), .O(o));
endmodule
"""
rtl = st.text_area("RTL source", default, height=300)

if st.button("Analyze and Convert", type="primary"):
    result = convert(rtl, source, target)
    report = make_report(rtl, result)

    c1, c2 = st.columns(2)
    c1.metric("Detected constructs", len(result.findings))
    c2.metric("Replacements", result.replacements)

    st.subheader("Converted RTL")
    st.code(result.converted_text, language="verilog")

    if result.warnings:
        st.subheader("Warnings")
        for w in result.warnings:
            st.warning(w)

    st.subheader("Unified diff")
    diff = "\\n".join(difflib.unified_diff(
        rtl.splitlines(),
        result.converted_text.splitlines(),
        fromfile="source.sv",
        tofile="converted.sv",
        lineterm=""
    ))
    st.code(diff or "No differences", language="diff")

    st.subheader("Conversion report")
    st.markdown(report)
    st.download_button("Download converted RTL", result.converted_text, "converted.sv")
    st.download_button("Download report", report, "conversion_report.md")
