module xilinx_example(
    input  wire clk_in,
    input  wire data_in,
    output wire clk_out,
    output wire data_out
);
    BUFG u_bufg (.I(clk_in), .O(clk_out));
    IBUF u_ibuf (.I(data_in), .O(data_out));
endmodule
