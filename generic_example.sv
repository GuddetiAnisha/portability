module generic_example(
    input  wire clk_in,
    output wire clk_out
);
    PORTABLE_CLKBUF u_clk (.I(clk_in), .O(clk_out));
endmodule
