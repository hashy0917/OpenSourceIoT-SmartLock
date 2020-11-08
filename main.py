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
    return render_template('top.html', title='OSSL toppage', status=status)

@app.route('/locking')
def locking():
    api_locking()
    #status = "lock"
    return status

@app.route('/unlock')
def unlock():
    api_unlock()
    time.sleep(second)
    api_locking()
    return status

#@app.route("/api/get/<key>", methods=["GET"])
#def api_get(key):

@app.route("/api/post/unlock", methods=["POST"])
def api_unlock():
    pi.set_servo_pulsewidth(servo_pin, 2350)

@app.route("/api/post/locking", methods=["POST"])
def api_locking():
    pi.set_servo_pulsewidth(servo_pin, 1450)

if __name__ == '__main__':
    app.run("0.0.0.0")
