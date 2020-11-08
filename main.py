import pigpio
import time
from flask import Flask, render_template

servo_pin = 4
second = 5

app = Flask(__name__)
pi = pigpio.pi()

'''
memo
500 = -90°
1450 = 0°
2350 = 90°
'''

@app.route('/')
def hello_world():
    pi.set_servo_pulsewidth(servo_pin, 1450) # 0°
    return '<html><body><h1>ようこそ</h1></body></html>'

@app.route('/locking')
def locking():
    pi.set_servo_pulsewidth(servo_pin, 500)
    return "lock"

@app.route('/unlock')
def unlock():
    pi.set_servo_pulsewidth(servo_pin, 2350)
    #time.sleep(second)
    #locking()
    return "unlock"

if __name__ == '__main__':
    app.run("0.0.0.0")
