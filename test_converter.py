from app.converter import convert
from app.analyzer import analyze

def test_detect_xilinx():
    text = "BUFG u0 (.I(clk), .O(gclk));"
    findings = analyze(text, "xilinx")
    assert any(f.construct == "Xilinx BUFG" for f in findings)

def test_xilinx_to_generic():
    text = "BUFG u0 (.I(clk), .O(gclk));"
    out = convert(text, "xilinx", "generic")
    assert "assign gclk = clk" in out.converted_text
    assert out.replacements == 1

def test_asic_to_generic():
    text = "CLKBUF_X1 u0 (.A(clk), .Y(gclk));"
    out = convert(text, "asic_generic", "generic")
    assert "assign gclk = clk" in out.converted_text

def test_generic_to_xilinx():
    text = "PORTABLE_CLKBUF u0 (.I(clk), .O(gclk));"
    out = convert(text, "generic", "xilinx")
    assert "BUFG u0" in out.converted_text

def test_unknown_construct_unchanged():
    text = "module x; UNKNOWN_CELL u0(); endmodule"
    out = convert(text, "xilinx", "generic")
    assert "UNKNOWN_CELL" in out.converted_text
