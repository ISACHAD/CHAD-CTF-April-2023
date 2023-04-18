# A Post A Day

*NOTE:* This challenge REQUIRES source code to solve.

This is more of a web programming challenge that envolves focusing on the URL and exploiting a logic bug

## Building

```
docker build . -t apple_a_day
```

## Running

```
docker run -p 4545:4545 apple_a_day
```

## Solving

- Go to website and play around with adding a post
- The add function is exploitable because the state structure is not completely random and it can be seen that the FLAG is associated with the 0th entry for id
- Get the sha256 hash of the state at id=0 which is `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9`
- Get the flag
