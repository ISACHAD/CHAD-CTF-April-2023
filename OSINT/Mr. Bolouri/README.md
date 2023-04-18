# Mr. Bolouri
**OSINT - Easy**

Wyatt Tauber

## Challenge

**This challenge involves Mr. Bolouri. Perform passive reconaissance only (do not interact with the persona or risk losing points).**

Hey! I’m a CS student at the University of Rochester. I am a fan of education, technology, and running. I’m also interested in music and movies. I've recently been optimizing my online presence while I'm searching for internships. You should check out my profiles sometime.

### Hint 1
Start by searching Google or Bing for some of the keywords above (Bing seems to have better results as of this writing).

Then, check out a few of my profiles and see if you can find parts of the flag!

### Flag
`CHAD{f0und_m3!}`

## Technique Overview

This challenge involves a simple trial and error search of online platforms. 

## Solve challenge:

Search "bolouri university of rochester" on Google or Bing (Bing seems to be better at this as of this writing, with most of Jackson Bolouri's profiles shown on the first and second pages).

Visit Jackson's [about.me](https://about.me/jbolou99) page first since it's the first result. It has links to three more pages, two of which contain pieces of the first flag.
- [Facebook](https://www.facebook.com/jackson.bolouri.1): No flag
- [TikTok](https://www.tiktok.com/@jabolou99): A video with "CHAD{f0und" and "1/2" in it
- [GitHub](https://github.com/jbolou99/): The "Profile" section of the page with "\_m3!}" and "2/2" in it

Assembling the pieces found from the profiles, the flag is `CHAD{f0und_m3!}`.
