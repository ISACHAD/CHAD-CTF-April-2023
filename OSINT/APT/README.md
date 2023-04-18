# APT
**OSINT - Medium**

Wyatt Tauber

_This challenge unlocks after Mr. Bolouri is solved._

## Challenge

**This challenge involves Mr. Bolouri. Perform passive reconaissance only (do not interact with the persona or risk losing points).**

I think somebody dumped my email password, so I had to change it. Can you find out who did it and what password they used?

### Hint 1
Peep my GitHub!

### Hint 2
Search Google or Bing for my email address.

### Flag
`CHAD{l1k3_my_4p7?}`

## Technique Overview

This challenge involves a bit more searching, but for specific info.

## Solve challenge:

Searching for Jackson's email address on Google or Bing would be a good way to identify if there's a dump related to his information available online. Google seems to be better at this as of this writing.

Jackson's email (jbolou99@gmail.com) is visible on his GitHub resume, possibly (but not necessarily) discovered via the "Recruiter Call" challenge.

Search for his email (in quotes) with Google.

One of the results is https://wyatttauber.com/chad.html. Use the find command to find his email on this page.

```
email=jbolou99@gmail.com:password=Q0hBRHtsMWszX215XzRwNz99
```

However, this isn't the flag. Examine the password in CyberChef. It is encoded Base64 for `CHAD{l1k3_my_4p7?}`.
