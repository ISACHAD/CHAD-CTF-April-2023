# Gigachat
**Reverse Engineering**

David Mentgen

## Challenge
\[Easy\]  
Initial Analysis: CHAD{g00d_j0b_cHeCkInG_tHe_sTr1nGs!}

\[Medium\]  
What's going on?: CHAD{i_l0v3_d3bUg_10gs!!}  
Connection: CHAD{c3rt1f1c@t3s_@r3_r3@11y_c00l!}

## Summary
This client contains several flags that can be found by using general RE skills.

## Initial Analysis
*All "GigaChat" challenges use the same file. There is no need to download it more than once.*

CHAD is starting development on a chat app. Can you do some initial analysis for us?

*Remember the flag is in CHAD{flag} format*

Author: D̸́̉3̷̐̌#1337

### Initial Analysis Walkthrough
Flag 1 is intended to be the easiest flag. Any tool that analyzes the binary's strings may reveal it.

Some tools that could be used to find this flag:  
- strings
- ghidra
- ida

## What's going on?
*All "GigaChat" challenges use the same file. There is no need to download it more than once.*

The app is acting weird.. How can we figure out what's going on?

*Remember the flag is in CHAD{flag} format*

Author: D̸́̉3̷̐̌#1337

### What's going on? Walkthrough

Flag 2 is located in the logs. This application has multiple levels of logging: 0 FATAL, 1 ERR, 2 WARN, 3 INFO, 4 DEBUG. By default, this application ships with level 3 logging (info) which means debug logs are not outputting.

First the user needs to find the log file. One way this could be done is by checking PROCMON.

Once the user finds the log, they’ll see all logs excluding DEBUG:

There is a subtle hint “Logging Level: INFO” that might tip users off that the logging level could be adjusted to reveal more information. Additionally, strings will reveal that there are “DEBUG” logs present in the binary.

When examining the log level in ghidra/ida, IDA seems to do a better job of showing what’s going on inside the WriteToLog (0x41C5C0) function:

Taking a closer look we can see that 0x41C611 seems to check the logging level (3)

To achieve the intended goal, the user only needs to increment the logging level one but really… any value greater than 3 will also work just fine. A user can simply just patch this number in IDA/Ghidra by changing the hex from 0x03 to any value greater than 0x03.

For this example, I’ve increased the logging level to 5:

NOTE: I’m not sure if IDA Free allows patching but Ghidra does. Extra creative users can also just take the offset from Ghidra/IDA and manually change the bits using xxd and vim.

Once this is done, executing the patched binary will reveal the next flag as a debug log:

NOTE: This log file says the level is “INFO” because I set the level to 0x05 which is not a valid debug level.. Therefore info is printed by default. If I had set it to a valid value of 0x04 it should then say it is using DEBUG level.

## Connection
*All "GigaChat" challenges use the same file. There is no need to download it more than once.*

GigaChat should be able to pull down messages from somewhere, right?

*Remember the flag is in CHAD{flag} format*

Author: D̸́̉3̷̐̌#6194

### Connection Walkthrough
This flag is intended to involve rebuilding a server and setting up necessary certificates.

When running the application, WireShark will reveal that it tries to reach out to SuperRealChatServer-im.chad.com

One way to handle this is editing Window’s etc/hosts and pointing that domain to 127.0.0.1.7 After this, we can start building our server. For this, I just use python3 flask.

Doing this we can see in WireShark that it wants to connect to port 42069:

Setting up a server on port 42069 still shouldn’t work. Depending on how their server is setup, it could look like “garbage” data coming from the client:

Debug logs should vaguely suggest there are “SSL Connection Problem”s occurring. This should tip people off to the fact that they need to generate a cert & key for their server. This can be done with openssl. I used the following command:

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

Luckily, using these in flask is easy:


The logs should look like a TLS handshake is occurring now, but still the client doesn’t seem to want to talk. Checking the logs again reveals that perhaps something is wrong with the certs:



Finding the “VerifyCerts” related strings in IDA can help identify the area that we need to pass:


With some digging around, users should eventually identify that there’s a string comparison that is made after receiving the server’s certificate. Function 0x4114D3 contains all of our secrets.



Here we can see all the strings needed to craft a “valid” certificate.
Together, this all forms: /C=CH/ST=AD{/L=c3rt1f1c@t3s/O=_@r3_/OU=r3@11y/CN=_c00l!}

This certificate can be crafted using the above openssl command and filling in each of the fields with the above information. Notice closely that the fields combine together to form a flag:
CHAD{c3rt1f1c@t3s_@r3_r3@11y_c00l!}
