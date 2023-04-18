# When in Rome...
**Networking - Medium**

Wyatt Tauber

## Challenge

[vIOS](https://1drv.ms/u/s!Al4cPlqRHIVDqstglL3_1jsmVn_5rQ?e=jgbfhy)

*If you don't VMWare Workstation or VirtualBox, I recommend installing [VMWare Workstation Player](https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html). You may need to install telnet.*

*Start the VM, connect to localhost:52099 via telnet, wait a minute or two, then hit enter a bunch. There is NO direct interaction via the VM interface.*

Chad keeps forgetting his password to log in to the router. Please recover it for him.

### Hint 1
This is Cisco IOS.

First, `enable` to access the admin console of the router.

Then, `show run` to view the current configuration.

### Hint 2
Here are some common types of encryption on Cisco IOS (may vary by device):

* 0 - an unencrypted password
* 4 - a SHA256 encrypted secret
* 5 - an MD5 encrypted secret
* 7 - a Vigenere encrypted secret
* 8 - a PBKDF2 hashed secret
* 9 - a Scrypt hashed secret

### Flag
```CHAD{v3n1_v163_v1c1}```

## Technique Overview

This challenge involves some basic knowledge of Cisco IOS and it's commands.

`enable` allows a user to manage the router
`show run` will show the current configuration of the router

Below is an outline of the common types of encryption on Cisco IOS (may vary by device):

* 0 - an unencrypted password
* 4 - a SHA256 encrypted secret
* 5 - an MD5 encrypted secret
* 7 - a Vigenere encrypted secret
* 8 - a PBKDF2 hashed secret
* 9 - a Scrypt hashed secret

Type 7 encryption on Cisco IOS can be cracked easily as is the Vigenere cipher.

### Solve challenge:

Show the running configuration of the device:

```
show run
```

Part of the output will be:

```
username admin privilege 15 nopassword
username chad password 7 096F66283D1E0141055D3B3C7A727B0C237310560B
```

You can use a variety of websites to crack the Vigenere cipher, but [this one](https://www.ifm.net.nz/cookbooks/passwordcracker.html) specifically for IOS is good.

The password is `CHAD{v3n1_v163_v1c1}`.
