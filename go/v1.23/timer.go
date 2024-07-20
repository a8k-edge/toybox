package main

import (
	"context"
	"fmt"
	"runtime"
	"time"
)

type token struct{}

func consumer(ctx context.Context, in <-chan token) {
	for {
		select {
		case <-in:
			// do stuff
		case <-time.After(time.Hour):
			// log warning
		case <-ctx.Done():
			return
		}
	}
}

// getAlloc returns the number of bytes of allocated
// heap objects (after garbage collection).
func getAlloc() uint64 {
	var m runtime.MemStats
	runtime.GC()
	runtime.ReadMemStats(&m)
	return m.Alloc
}

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	tokens := make(chan token)
	go consumer(ctx, tokens)

	memBefore := getAlloc()

	for range 1_000_000 {
		tokens <- token{}
	}

	memAfter := getAlloc()
	memUsed := memAfter - memBefore
	fmt.Printf("Memory used: %d KB\n", memUsed/1024)
}
