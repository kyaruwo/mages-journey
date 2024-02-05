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

	var lvl, xp, g, hp, atk = 1, 0, 0, 8, 4

	fmt.Println("lvl", lvl)
	fmt.Println(" xp", xp)
	fmt.Println("  g", g)
	fmt.Println(" hp", hp)
	fmt.Println("atk", atk)
}
