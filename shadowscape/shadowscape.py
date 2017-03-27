import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import serial

app = Flask(__name__)
socketio = SocketIO(app)

turnOn = False


@app.route('/')
def shadowscape():
    return render_template('shadowscape.html')


@app.route('/animation')
def slider():
    return render_template('animation.html')


@socketio.on('day update')
def day_update(message):
    ser = serial.Serial("/dev/cu.usbmodem1421", 9600)

    day_of_week = message['day']
    emit('day become', message, broadcast=True)

    # Testing using blink
    blink_arduino_writer(ser, day_of_week)

    # Execute the day for arduino
    # day_arduino_writer(ser, day_of_week)

    print('socket :' + day_of_week)
    time.sleep(3)


def blink_arduino_writer(ser, day_of_week):
    if day_of_week == 'sunday':
        print('SUNDAY')
        ser.write("0".encode())

    elif day_of_week == 'monday':
        print('MONDAY')
        ser.write("1".encode())

    elif day_of_week == 'tuesday':
        ser.write("0".encode())

    elif day_of_week == 'wednesday':
        print('WEDNESDAY')
        ser.write("1".encode())

    elif day_of_week == 'thursday':
        print('THURSDAY')
        ser.write("0".encode())

    elif day_of_week == 'friday':
        print('FRIDAY')
        ser.write("1".encode())

    elif day_of_week == 'saturday':
        print('SATURDAY')
        ser.write("0".encode())

    elif day_of_week == 'now':
        print('NOW')
        ser.write("1".encode())


def day_arduino_writer(ser, day_of_week=0):

    if day_of_week == 'sunday':
        print('SUNDAY')
        ser.write("0".encode())

    elif day_of_week == 'monday':
        print('MONDAY')
        ser.write("1".encode())

    elif day_of_week == 'tuesday':
        ser.write("2".encode())

    elif day_of_week == 'wednesday':
        print('WEDNESDAY')
        ser.write("3".encode())

    elif day_of_week == 'thursday':
        print('THURSDAY')
        ser.write("4".encode())

    elif day_of_week == 'friday':
        print('FRIDAY')
        ser.write("5".encode())

    elif day_of_week == 'saturday':
        print('SATURDAY')
        ser.write("6".encode())

    elif day_of_week == 'now':
        print('NOW')
        ser.write("7".encode())


if __name__ == "__main__":
    # lets launch our web page!
    # do 0.0.0.0 so that we can log into this web page
    # using another computer on the same network later
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')