package main

import (
    "fmt"
    "github.com/ahmdrz/goinsta/v2"
)

func main() {
    insta := goinsta.New("username", "password")

    if err := insta.Login(); err != nil {
        panic(err)
    }

    fmt.Println("Logged in as:", insta.Account.Username)
}
