# Ice Court Heist
**Forensics - Medium**

Wyatt Tauber

## Challenge

The Crows' demolitions expert is operating under cover during the Ice Court heist. We have reason to believe they hid both his names in this map. Can you find them?

### Hint 1
This is a steganography challenge. A popular tool for steganography is [steghide](https://steghide.sourceforge.net/). The opposite of steg*hide* would be steg____.

### Hint 2
Assuming you've cracked the password and extracted the second image from the first using [stegseek](https://github.com/RickdeJager/stegseek), analyze the second image in a way other than viewing it. There are lots of methods for hiding data in spaces that the image doesn't use. Look for encoded data.

### Flag
```CHAD{v4n_3ck_or_h3ndr1cks?}```

## Technique Overview
[Steganography](https://en.wikipedia.org/wiki/Steganography) is the practice of hiding data inside a file not indended to carry such data.

<img src="https://steghide.sourceforge.net/images/logo.png" alt="steghide logo" width="100"/>

[Steghide](https://steghide.sourceforge.net/) is a popular tool used for steganography. It encrypts files using AES.

This image, grishaverse.jpg, contains a smaller image hidden via steghide. The smaller image, wylan.webp, has a base64-encoded flag appended to the end of it.

### Solve challenge:

Tools needed:
[Stegseek](https://github.com/RickdeJager/stegseek)

The statement "...in this image.." implies some sort of image manipulation. Users may investigate the metadata or structure of the image itself first, but the large file size of this JPEG should indicate steganography. Check to see if there might be an encrypted file embedded inside this image:

```
wyatt@WYATT-DESKTOP:/img$ stegseek --seed grishaverse.jpg
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found (possible) seed: "50c3e77c"
        Plain size: 208.2 KB (compressed)
        Encryption Algorithm: rijndael-128
        Encryption Mode:      cbc
```

This looks promising. However, if the user attempts to use steghide to extract the file, they'll be prompted for a passphrase, which they don't have:

```
wyatt@WYATT-DESKTOP:/img$ steghide info grishaverse.jpg
"grishaverse.jpg":
  format: jpeg
  capacity: 550.8 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
```

Instead, use stegseek again with a wordlist to try to crack the passphrase and extract the file:

[rockyou.txt](https://1drv.ms/t/s!Al4cPlqRHIVDqsthfx2Z3my4c2zPiA?e=OC2c87)

```
wyatt@WYATT-DESKTOP:/img$ stegseek --crack grishaverse.jpg rockyou.txt output
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "wylan")

[i] Original filename: "wylan.webp".
[i] Extracting to "output".
```

Running ```file``` on ```output``` confirms that this is a WebP image.

```
wyatt@WYATT-DESKTOP:/img$ file output
output: RIFF (little-endian) data, Web/P image
```

Unfortunately, opening this file doesn't show the flag. Doing an image search for it shows [this result](https://thegrishaverse.fandom.com/wiki/Wylan_Van_Eck?file=Wylan_and_Kuwei_by_Kevin_Wada.png) online. It looks like the extracted image is 17k larger.

Compare the original and changed files. I like [Beyond Compare](https://www.scootersoftware.com/index.php) (free trial) for this. Since doing an image comparison yields no changes, try doing a hex comparison. There's a bunch of data at the end of the file, starting with:

```
Q0hBRHt2NG5fM2NrX29yX2gzbmRyMWNrcz99...=
```

Examining this string in CyberChef with Magic states that this is Base64:

```
CHAD{v4n_3ck_or_h3ndr1cks?}
```

You also could have just used `strings` (or [forensically](https://29a.ch/photo-forensics/#strings)'s string extractor, if you were really getting into the whole image analysis thing) and noticed the abnormally long string near the bottom.