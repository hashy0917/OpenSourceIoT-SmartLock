#!/usr/bin/env python3

from flask import Flask, render_template
import pigpio
import time

servo_pin = 4
second = 5

app = Flask(__name__)
pi = pigpio.pi()

status = "lock"

'''
memo
500 = -90°
1450 = 0°
2350 = 90°
'''

@app.route('/')
def hello_world():
    pi.set_servo_pulsewidth(servo_pin, 1450)
    return render_template('hello.html', title='flask test', status=status)

@app.route('/locking')
def locking():
    pi.set_servo_pulsewidth(servo_pin, 1450)
    #status = "lock"
    return status

@app.route('/unlock')
def unlock():
    pi.set_servo_pulsewidth(servo_pin, 2350)
    #status = "unlock"
    time.sleep(second)
    locking()
    #status = "lock"
    return status

#@app.route("/api/get/<key>", methods=["GET"])
#def api_get(key):

@app.route("/api/post/unlock", methods=["POST"])
def api_unlock():
    unlock()
    return status

@app.route("/api/post/locking", methods=["POST"])
def api_locking():
    locking()
    return status

if __name__ == '__main__':
    app.run("0.0.0.0")
