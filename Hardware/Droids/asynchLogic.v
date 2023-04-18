module asynchLogic(
    input  wire A, B, C, D,
    output wire R
);

wire tempA, tempB, tempC, tempD;

assign tempA = (~C & ~D);
assign tempB = (D & B);
assign tempC = (~A & ~B & ~D);
assign tempD = (A & ~B & ~C);

assign  R = ~(tempA | tempB | tempC | tempD);



endmodule