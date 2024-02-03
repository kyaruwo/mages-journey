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

	fmt.Println("lvl")
	fmt.Println(" xp")
	fmt.Println("  g")
	fmt.Println(" hp")
	fmt.Println("atk")
}
