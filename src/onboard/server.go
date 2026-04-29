package main

import (
	"TSN/src/board"
	"fmt"
)

func main() {
	fmt.Println("----- Agent start -----")
	agent := board.Agent{}
	agent.Init(0, "0.0.0.0", 54321)
}
