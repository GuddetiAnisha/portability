module asic_example(
    input  wire clk_in,
    output wire clk_out
);
    CLKBUF_X1 u_clk (.A(clk_in), .Y(clk_out));
endmodule
