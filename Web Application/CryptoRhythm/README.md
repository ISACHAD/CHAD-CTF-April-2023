```
   _____ _______     _______ _______ ____  _____  _    ___     _________ _    _ __  __
  / ____|  __ \ \   / /  __ \__   __/ __ \|  __ \| |  | \ \   / /__   __| |  | |  \/  |
 | |    | |__) \ \_/ /| |__) | | | | |  | | |__) | |__| |\ \_/ /   | |  | |__| | \  / |
 | |    |  _  / \   / |  ___/  | | | |  | |  _  /|  __  | \   /    | |  |  __  | |\/| |
 | |____| | \ \  | |  | |      | | | |__| | | \ \| |  | |  | |     | |  | |  | | |  | |
  \_____|_|  \_\ |_|  |_|      |_|  \____/|_|  \_\_|  |_|  |_|     |_|  |_|  |_|_|  |_|
                      V2.1 Private Paypal scam page [PRV8 FIX]
```
# Web - Easy and Medium

Wyatt Tauber

This is a real web application that I [stole from a scammer](https://blog.wyatttauber.com/cryptorhythm-analyzing-and-disrupting-a-paypal-scam-with-love-and-toucans-2d9f59b5d6ae) back in 2020. If participants find the blog post, they'll only be able to solve easy 2 at most as the rest is added functionality, and this seems fine to me.

The portion of the "mhamdi_manager" application at http://chadctf-web-various-cryptorhythm.chals.io/assets/img.php that is a reverse shell will trigger Windows Defender (even though it's harmless), so it's archived in a .tar.gz file that gets extracted once inside the container. Just a warning if you extract it yourself!

## Challenges

### CryptoRhythm 1 - Easy - Lucas The Spidering App

There's this scammer who thinks he's really clever and has built an impenetrable PayPal scam. Prove him wrong by finding his hidden page!

**Do not deface the website. Do not make changes to the website. Operations are logged. This site will be reset frequently.**

**Do not enter real PII. The information collection features of this application have been disabled, but this still used to be a real PayPal scam application.**

### Hint 1
Use a web spider or fuzzer to find hidden pages on the website. I like wfuzz.

You may need to fuzz a few times at various depths.

### Flag
```CHAD{5up3r_l337_4dm1n_p463}```

### CryptoRhythm 2 - Medium - Where's my mhamdi?
_This challenge unlocks after CryptoRhythm 1 is solved._

Not everything is visible in HTML. Use your newfound access to find the flag.

**Do not deface the website. Do not make changes to the website. Operations are logged. This site will be reset frequently.**

**Do not enter real PII. The information collection features of this application have been disabled, but this still used to be a real PayPal scam application.**

### Hint 1
Explore the mhamdi_manager a bit more. What can you view with it?

### Hint 2
Take a look at https://chadctf-web-various-cryptorhythm.chals.io/lang.php

### Flag
```CHAD{f4ncy_f1l3_3d170r}```

## Technique Overview
_Replace "localhost" with the IP address of the application, if necessary._

### CryptoRhythm 1 - Easy:

I edited the "mhamdi_manager" page at http://localhost/assets/img.php to include the flag at the bottom. It can be found via [spidering/fuzzing] (https://en.wikipedia.org/wiki/Web_crawler) common URL names.

### CryptoRhythm 2 - Medium:

After finding the "mhamdi_manager" page, use the built-in file browser to view the PHP for each of the pages. https://chadctf-web-various-cryptorhythm.chals.io/lang/index.php has a message indicating that the easy challenge needs to be solved before finding this flag, and below it is an obfuscated PHP string that is commented out (this is not visible when just browing to the page in a browser). Comment in the string so it is de-obfuscated, and the flag will be visible.

## Solve challenges:
_Replace "localhost" with the IP address of the application, if necessary._

### CryptoRhythm 1 - Easy:

1. Open a URL spider/fuzzer. I like wfuzz beacuse it allows significant customization as opposed to those in BurpSuite and ZAP.

2. Fuzz http://localhost/. These settings tell wfuzz to use a wordlist as a payload (-z file,/usr/share/wfuzz/wordlist/general/common.txt) and hide 404 messages (–hc 404).

```
┌──(rtfm)─(kali㉿kali)-[~]
└─$ wfuzz -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://localhost/FUZZ

********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://localhost/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                          
=====================================================================

000000029:   301        9 L      28 W       320 Ch      "account"                                                                                                        
000000032:   301        9 L      28 W       320 Ch      "actions"                                                                                                        
000000076:   301        9 L      28 W       319 Ch      "assets"                                                                                                         
000000417:   301        9 L      28 W       316 Ch      "inc"                                                                                                            
000000434:   301        9 L      28 W       320 Ch      "install"                                                                                                        

Total time: 0.548242
Processed Requests: 951
Filtered Requests: 946
Requests/sec.: 1734.635
```

3. There are a couple pages here. We can visit them, but they don't provide much useful information. Try fuzzing each one individually. Eventually, we try http://chadctf-web-various-cryptorhythm.chals.io/assets/FUZZ:

```
┌──(rtfm)─(kali㉿kali)-[~]
└─$ wfuzz -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://localhost/assets/FUZZ

********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://localhost/assets/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                          
=====================================================================

000000224:   301        9 L      28 W       323 Ch      "css"                                                                                                            
000000414:   301        9 L      28 W       323 Ch      "img"                                                                                                            
000000456:   301        9 L      28 W       322 Ch      "js"                                                                                                             

Total time: 0.579651
Processed Requests: 951
Filtered Requests: 948
Requests/sec.: 1640.640
```

4. Browse to these pages. The hidden page is at http://chadctf-web-various-cryptorhythm.chals.io/assets/img and the flag is at the bottom:

```
CHAD{5up3r_l337_4dm1n_p463}
```

### CryptoRhythm 2 - Medium:

1. You can now explore the site more easily with the "mhamdi_manager" application. Looking around the top-level directories a bit should eventually bring you to ```/lang/en.php```:

```
<!DOCTYPE html>
<html>
<body>

oopsies no flag here yet... go solve the easy challenges first and come back here a different way

<?php
~~ removed this code because it sets off Windows Defender, but the code can be seen at this location ~~
*/
?>

</body>
</html>
```

2. Looking at the site https://chadctf-web-various-cryptorhythm.chals.io/lang.php gives a hint on how to solve the challenge: 

```
<html><head></head><body>

oopsies no flag here yet... go solve the easy challenges first and come back here a different way

</body></html>
```

3. There is encoded PHP on the page, but it's commented out and thus won't appear in the HTML. Use mhamdi_manager to view the encoded PHP.

4. Use a PHP parser like the one from W3Schools to evaluate the code:

```
CHAD{f4ncy_f1l3_3d170r}
```
