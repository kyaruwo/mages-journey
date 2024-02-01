package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	clear := exec.Command("cmd", "/c", "cls")
	clear.Stdout = os.Stdout
	clear.Run()

	fmt.Println("=o= mages journey =o=")
}
