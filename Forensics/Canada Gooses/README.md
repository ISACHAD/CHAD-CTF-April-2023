# Canada Gooses
**Forensics - Easy**

Wyatt Tauber

## Challenge

Youse guys heard what Coach is up to at the country club? That ankle-sock wearin' sally and a couple other 10-ply folk up there says there's too much crap from Canada gooses on the golf course. But get this: to curb the amounts of craps from Canada gooses, that degen has put the wheels in motion to oil and grease up the eggs so they won't hatch!!! _smashes beer bottle_

Help the hicks get on down to the town board meeting and have a scrap. Only problem is, Coach must've had the skids do some computer so nobody can read the flyer to find the time or location. But you're good with computer too, right?

"If you got a problem with Canada gooses, you got a problem with me..."

### Hint 1
The flyer and the redaction bar are two separate PDF objects. Is there a way to extract only one of them?

### Flag
```CHAD{4nd_1_5u66357_y0u_l37_7h47_0n3_m4r1n473}```

## Technique Overview

This PDF was made by making an image containing the flyer, then pasting that image into a PDF and adding the redaction bar.

To solve this challenge, the only thing that needs to be recognized is that the flyer and the redaction bar are two separate images in the PDF. The original image can then be extracted from it.

Editing as well as copy and paste are disabled in this PDF to prevent copying the flag out.

Password for editing the PDF (if needed): wyatttauber

### Solve challenge:

Use any PDF analysis tool to extract the original image:

```
wyatt@WYATT-DESKTOP:/pdf$ ls
'LETTERKENNY TOWN BOARD SPECIAL MEETING.pdf'
wyatt@WYATT-DESKTOP:/pdf$ pdfimages "LETTERKENNY TOWN BOARD SPECIAL MEETING.pdf" ./
wyatt@WYATT-DESKTOP:/pdf$ ls
 -000.ppm   -001.ppm  'LETTERKENNY TOWN BOARD SPECIAL MEETING.pdf'
 wyatt@WYATT-DESKTOP:/pdf$ gimp -000.ppm
 ```
 
 The flag is shown in the image, ```CHAD{4nd_1_5u66357_y0u_l37_7h47_0n3_m4r1n473}```
