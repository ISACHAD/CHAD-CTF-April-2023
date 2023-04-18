# Mr. Bolouri
**OSINT - Hard**

Wyatt Tauber

_This challenge unlocks after Mr. Bolouri is solved._

## Challenge

**This challenge involves Mr. Bolouri. Perform passive reconaissance only (do not interact with the persona or risk losing points).**

My favorite spot to relax involves a bit of a hike. Come with me sometime!

_Wrap the name of the location Mr. Bolouri likes to hike at in `CHAD{}`. Do not include special characters (if applicable)._

### Hint 1
Peep my Facebook!

### Hint 2
[FCC Antenna Structure Registrations Database](https://wireless2.fcc.gov/UlsApp/AsrSearch/asrRegistrationSearch.jsp)

### Hint 3
Map the results and switch to satellite view. Look for a wooded area with three towers. The only matching location is in southeast Rochester.

### Flag
`CHAD{Pinnacle Hill}`

## Technique Overview

This challenge involves a brief online search and then a more complex search of the online FCC ASR, or a similar database.

## Solve challenge:

Jackson has a background on his Facebook page showing him in the woods facing three large towers with the caption "Such a relaxing hike".

Identify these three towers by searching the FCC [Antenna Structure Registrations (ASR)](https://wireless2.fcc.gov/UlsApp/AsrSearch/asrRegistrationSearch.jsp) database. Conduct an advanced search for towers in the Rochester, NY area that are constructed.

Map the results and switch to satellite view. Look for a wooded area with three towers. The only matching location is in southeast Rochester, known as Pinnacle Hill.

The flag is `CHAD{Pinnacle Hill}`.
