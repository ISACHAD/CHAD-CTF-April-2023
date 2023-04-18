module modA
  #(parameter UNTZ = 32,
	      YOYO = 1024,
	      GILD = 768)
    (input  wire clk,
     input  wire rst,
     input  wire moo,
     output wire [10:0] ym,
     output wire [10:0] sl);
   
   reg [10:0] 		yyy, h;
   wire [10:0] 		od, ne;
   
   reg 			re, it;
   wire 		no, lk;
   
   wire [10:0] 		en, sn;
   wire 		pt, zz;
   
   always @(posedge clk or posedge rst)
	if (rst) 
	  begin
	     yyy = YOYO / 2;
	     h = GILD / 2;
	     re = 1'b0;     
	     it = 1'b0;	     
	  end
	else
	  begin
	     yyy = od;
	     h = ne;
	     re = no;
	     it = lk;
	  end
   
   assign en       = (re) ? yyy + 1'b1 : yyy - 1'b1;
   assign sn       = (it) ? h + 1'b1 : h - 1'b1;
   
   assign pt    = (en <= UNTZ) || (en >= (YOYO - UNTZ));
   assign zz    = (sn <= UNTZ) || (sn >= (GILD - UNTZ));

   assign no = (moo & pt) ? ~re : re;
   assign lk = (moo & zz) ? ~it : it;
   
   assign od     = (moo) ? en : yyy;
   assign ne     = (moo) ? sn : h;

   assign ym     = yyy;
   assign sl     = h;

endmodule
