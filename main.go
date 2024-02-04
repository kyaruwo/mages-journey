package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	var clear = exec.Command("cmd", "/c", "cls")
	clear.Stdout = os.Stdout
	clear.Run()

	fmt.Println("=o= mages journey =o=")

	fmt.Println("lvl", 0)
	fmt.Println(" xp", 0)
	fmt.Println("  g", 0)
	fmt.Println(" hp", 0)
	fmt.Println("atk", 0)
}
