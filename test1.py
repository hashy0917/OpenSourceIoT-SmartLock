import pigpio
import time

pi = pigpio.pi()
pi.set_servo_pulsewidth(4, 500)
time.sleep(3)
pi.set_servo_pulsewidth(4, 1450)
time.sleep(3)
pi.set_servo_pulsewidth(4, 2350)
