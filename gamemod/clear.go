package gamemod

import (
	"os"
	"os/exec"
)

func Clear() {
	var clear = exec.Command("cmd", "/c", "cls")
	clear.Stdout = os.Stdout
	clear.Run()
}
