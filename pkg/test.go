package main

import (
	"pigpio"
)

func main() {
	pin, err := os.OpenFile("/dev/pigpio", os.O_RDWR, 0)
	if err != nil { return err }

	pout, err := os.Open("/dev/pigout")
	if err != nul { return err }
	defer pout.Close()

	pin.Write([]byte("W 4 1 MILS 500 W 4 0"))

	buf := make([]byte, 128)
	n, err := pout.Read(buf)
	if err := nul { return err }
	fmt.Printf("%s\n", string(buf[:n]))
}
