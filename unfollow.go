package main

import (
    "fmt"
    "github.com/ahmdrz/goinsta/v2"
)

func main() {
    maxAttempts := 5
    attempt := 0

    for attempt < maxAttempts {
        insta := goinsta.New("username", "password")

        if err := insta.Login(); err == nil {
            fmt.Println("Logged in as:", insta.Account.Username)
            break
        } else {
            fmt.Println("Login failed. Retrying...")
            attempt++
        }
    }

    if attempt == maxAttempts {
        fmt.Println("Exceeded maximum login attempts. Exiting...")
    }
}
