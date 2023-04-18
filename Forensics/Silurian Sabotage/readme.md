# Silurian Sabotage
**Forensics - Hard**

Wyatt Tauber

## Challenge

[tardis_memory_core](https://1drv.ms/u/s!Al4cPlqRHIVDqstjCmGzPe9Bxwd8BQ?e=abF6Xz)

The Silurians gained access to the TARDIS's telepathic circuits and infected it with a rootkit. In order to remove the malware, the Doctor needs to locate it in the TARDIS's memory core. Can you help?

### Hint 1
Referenceing memory indicates that you've been provided a memdump. You can use Volatility3 to analyze it, but you'll need some additional files too.

### Hint 2
Check the banner of the image to determine the symbol table to use:

```
python3 vol.py -f {image path} banners
```

Download the appropriate image from the [Volatility3 Linux ISF server](https://isf-server.techanarchy.net/) and put it in the appropriate directory.

### Hint 3
Check for the rootkit using Volatility's ```linux.check_modules``` command. You may need to view the location in a memory viewer to see full contents of the address.

### Flag
```CHAD{r3pt1le_r00tk1ts_r3v1v3d}```

## Technique Overview
<img src="https://i.pinimg.com/originals/dc/cd/91/dccd91a198d69545c00c4204635e8eee.png" alt="Volatility Logo" width="100"/>

**[Volatility3](https://www.volatilityfoundation.org/)**

Volatility is the world's most widely used framework for extracting digital artifacts from volatile memory (RAM) samples. This exercise challenges the user to obtain a symbol table for the proper Linux distribution and analyze the provided memory image with Volatility3 to find the rootkit module.

## Implementation Details

1. Download and install [Ubuntu 18.04 LTS](https://releases.ubuntu.com/18.04/)
2. Download the [Reptile](https://github.com/f0rb1dd3n/Reptile) rootkit and prerequisites:
```
sudo apt install build-essential libncurses-dev linux-headers-$(uname -r) git
git clone https://github.com/f0rb1dd3n/Reptile.git
```
3. Hide the flag as the module name:
```
kernel/Kbuild:
  MODNAME		                        ?= {FLAG}
Makefile:
  PARASITE ?= $(BUILD_DIR)/{FLAG}.ko
```
4. Make and install the rootkit:
```
cd Reptile
make menuconfig
make
sudo make install
```
5. Delete the rootkit install files and clear history:
```
cd ..
rm -rf Reptile
history -c
clear
```
6. Take the memory image with [LiME](https://github.com/504ensicsLabs/LiME) in the ```lime``` format:
```
git clone https://github.com/504ensicsLabs/LiME.git
cd LiME/src
make
insmod ./lime.ko "path=../{image name} format=lime"
```

### Solve challenge:
**Follow the steps in the [Volatility Linux Tutorial](https://volatility3.readthedocs.io/en/latest/getting-started-linux-tutorial.html).**

1. Unzip the challenge.

2. Download and install Volatility3:
```
git clone https://github.com/volatilityfoundation/volatility3.git
```
3. Check the banner of the image to determine the symbol table to use:
```
python3 vol.py -f {image path} banners
```
This should produce the banner "Linux version 4.15.0-20-generic (buildd@lgw01-amd64-039) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018 (Ubuntu 4.15.0-20.21-generic 4.15.17)".

4. Download the Ubuntu 18.03 LTS image from the [Volatility3 Linux ISF server](https://isf-server.techanarchy.net/) by searching for the banner. It should be the file name "4.15.0-20-generic_4.15.0-20.21_amd64.json.xz".

5. Extract the file.

6. Place the file in ```volatility3/symbols```

7. Check for the rootkit using ```linux.check_modules```:
```
python3 vol.py -f {image path} linux.check_modules
```
This should generate the flag at ```0xffffc03ad400```. View the location in any memory viewer to see the full flag.

