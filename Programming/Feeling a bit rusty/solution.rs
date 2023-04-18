const INPUT: &str = "143x44x52, 55x39x27, 19x48x64, 68x83x74, 29x14x70, 45x17x95, 32x57x48, 33x92x44, 85x25x10, 93x25x97, 99x21x48, 46x13x31, 6x30x10, 9x21x22, 64x42x91, 21x32x19, 56x80x5, 45x9x19, 50x77x94, 35x86x13, 58x60x10, 73x35x35, 42x10x59, 18x88x39, 23x98x27, 65x67x47, 27x89x19, 70x90x90, 11x30x98, 56x55x29, 37x40x24, 99x95x80, 98x7x82, 34x39x73, 34x16x57, 17x28x39, 42x57x99, 42x37x7, 78x53x12, 60x41x35, 7x94x17, 7x33x19, 34x46x41, 46x20x26, 14x29x36, 34x33x43, 78x30x14, 75x96x85, 33x53x94, 61x19x32";
fn main() {
    let mut num_gallons = 0;

    let mut sq_ft = 0;
    for part in INPUT.split(", ") {
        //let dimm = parse_data::<i32>(part, 'x');
        let dimm:Vec<i32> = part.split("x").map(|x| x.parse::<i32>().ok().unwrap()).collect();
        let surface1 = dimm[0] * dimm[1] * 2;
        let surface2 = dimm[1] * dimm[2] * 2;
        let surface3 = dimm[0] * dimm[2] * 2;
        sq_ft += surface1 + surface2 + surface3;
        // println!("x: {}, y: {}, x:{}, area: {}", dimm[0], dimm[1], dimm[2], surface1 + surface2 + surface3 );
    }
    println!("CHAD{{{}}}", sq_ft/400);
}
