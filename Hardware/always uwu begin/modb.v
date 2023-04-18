module modB
  #(parameter LOL = 16)
    (input wire clk,
    input wire rst,
    input wire [10:0]  n,
    input wire [10:0]  m,
    input wire [10:0]  o,
    input wire [10:0]  p,
    output wire        q);

   wire [10:0] 	       a, b, c, d;
   wire 	       t;
   wire [4:0] 	       i, r;
   reg [31:0] 	       uwu;
   wire [4:0] 	       wow;
   wire                stu;
   
   assign a     = n - LOL;
   assign b    = n + LOL;
   assign c      = m - LOL;
   assign d   = m + LOL;
   
   assign t     = (o >= a) && (o <= b) &&
		       (p >=  c) && (p <= d);
   
   assign r     = t ? o - a : 0;
   assign i     = t ? p - c : 0;
   
   assign wow   = i;
   assign stu    = uwu[r];
   
   assign q = stu;

   always @*
     case (wow)
       5'o00: uwu = 32'd0001044480; 
       5'o01: uwu = 32'd0008388096; 
       5'o02: uwu = 32'd0016776960; 
       5'o03: uwu = 32'd0067108800; 
       5'o04: uwu = 32'd0134217696; 
       5'o05: uwu = 32'd0268435440; 
       5'o06: uwu = 32'd0536870904; 
       5'o07: uwu = 32'd0536870904; 
       5'o10: uwu = 32'd1073741820; 
       5'o11: uwu = 32'd2147483646; 
       5'o12: uwu = 32'd2147483646; 
       5'o13: uwu = 32'd2147483646; 
       5'o14: uwu = 32'd4294967295; 
       5'o15: uwu = 32'd4294967295; 
       5'o16: uwu = 32'd4294967295; 
       5'o17: uwu = 32'd4294967295; 
       5'o20: uwu = 32'd4294967295; 
       5'o21: uwu = 32'd4294967295; 
       5'o22: uwu = 32'd4294967295; 
       5'o23: uwu = 32'd4294967295; 
       5'o24: uwu = 32'd2147483646; 
       5'o25: uwu = 32'd2147483646; 
       5'o26: uwu = 32'd2147483646; 
       5'o27: uwu = 32'd1073741820; 
       5'o30: uwu = 32'd0536870904; 
       5'o31: uwu = 32'd0536870904; 
       5'o32: uwu = 32'd0268435440; 
       5'o33: uwu = 32'd0134217696; 
       5'o34: uwu = 32'd0067108800; 
       5'o35: uwu = 32'd0016776960; 
       5'o36: uwu = 32'd0008388096; 
       5'o37: uwu = 32'd0001044480; 
     endcase

endmodule 

