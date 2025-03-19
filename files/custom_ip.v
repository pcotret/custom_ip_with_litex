module custom_ip (
    input [31:0] a,  // 8-bit input a
    input [31:0] b,  // 8-bit input b
    output [31:0] c  // 8-bit output c
);
    // Add a and b, and assign the result to c
    assign c = a+b;
endmodule