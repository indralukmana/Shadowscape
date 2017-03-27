import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import serial

app = Flask(__name__)
socketio = SocketIO(app)

turnOn = False

# day_of_week = ""

# initialize connection to Arduino
# if your arduino was running on a serial port other than '/dev/ttyACM0/'
# declare: a = Arduino(serial_port='/dev/ttyXXX')
# a = Arduino(serial_port='/dev/cu.usbmodem1411')
time.sleep(3)

# declare the pins we're using
LED_PIN = 13
ANALOG_PIN = 0

# initialize the digital pin as output
# a.set_pin_mode(LED_PIN, 'O')

print('Arduino initialized')


@app.route('/<day>')
def shadowscape(day):
    print("STARTING")
    ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

    print(day)
    #
    # if day is '1':
    #     print('SUNDAY')
    #     ser.write("1".encode())
    #
    # elif day == '2':
    #     print('MONDAY')
    #     ser.write("2".encode())
    #
    # elif day == '3':
    #     print('TUESDAY')
    #     ser.write("3".encode())
    #
    # elif day == '4':
    #     print('WEDNESDAY')
    #     ser.write("4".encode())
    #
    # elif day == '5':
    #     print('THURSDAY')
    #
    # elif day == '6':
    #     print('FRIDAY')
    #
    # elif day == '7':
    #     print('SATURDAY')
    #
    # elif day == '0':
    #     print('NOW')
    #
    # else:
    #     pass

    return render_template('shadowscape.html')


@app.route('/slider')
def slider():
    return render_template('index.html', **values)


@socketio.on('value changed')
def value_changed(message):
    emit('update value', message, broadcast=True)
    print(message)


@socketio.on('day update')
def day_update(message):
    ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

    day_of_week = message['day']
    emit('day become', message, broadcast=True)

    blink_arduino_writer(ser, day_of_week)

    print('socket :' + day_of_week)


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