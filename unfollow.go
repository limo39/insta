package main

import (
	"fmt"
	"github.com/ahmdrz/goinsta/v2"
	"sync"
)

func main() {
	username := "your_username"
	password := "your_password"
	maxUnfollows := 100 // Maximum number of users to unfollow
	numWorkers := 10   // Number of concurrent unfollow workers
	done := make(chan bool)

	insta := goinsta.New(username, password)

	if err := insta.Login(); err != nil {
		panic(err)
	}

	fmt.Println("Logged in as:", insta.Account.Username)

	if err := insta.Account.Following().Error(); err != nil {
		panic(err)
	}

	following := insta.Account.Following().Users
	totalUnfollows := min(maxUnfollows, len(following))

	var wg sync.WaitGroup
	wg.Add(numWorkers)

	unfollowedCount := 0
	unfollowedMutex := sync.Mutex{}

	for i := 0; i < numWorkers; i++ {
		go func() {
			defer wg.Done()

			for {
				unfollowedMutex.Lock()

				if unfollowedCount >= totalUnfollows {
					unfollowedMutex.Unlock()
					return
				}

				user := following[unfollowedCount]
				unfollowedCount++
				unfollowedMutex.Unlock()

				if err := user.Unfollow(); err == nil {
					fmt.Println("Unfollowed:", user.Username)
				} else {
					fmt.Println("Failed to unfollow:", user.Username, err)
				}
			}
		}()
	}

	go func() {
		wg.Wait()
		close(done)
	}()

	<-done
	fmt.Println("Unfollow process completed.")
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
