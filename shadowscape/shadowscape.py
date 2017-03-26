import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import serial

# from pyduino import Arduino
app = Flask(__name__)
socketio = SocketIO(app)

values = {
    'slider1': 25,
    'slider2': 0,
}

day_of_week = ""

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


# we are able to make 2 different requests on our web page
# GET = we just type in the url
# POST = some sort of form submission like a button
# @app.route('/')
@app.route('/<day>')
def shadowscape(day):
    print("STARTING")
    # if we make a post request on the web page aka press button then do stuff
# if day is not None:
    ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

    print(day)
    # if we press the turn on button
    if day is '1':
        print('SUNDAY')
        # turn on LED on arduino
        # a.digital_write(LED_PIN, 1)
        # a.digital_write_value(1)
        ser.write("1".encode())
    # if we press the turn off button
    elif day == '2':
        print('MONDAY')
        # a.analog_write_value(2)
        ser.write("2".encode())
        # turn off LED on arduino
        # a.digital_write(LED_PIN, 0)

    elif day == '3':
        print('TUESDAY')
        ser.write("3".encode())

        # a.analog_write_value(3)

    elif day == '4':
        print('WEDNESDAY')
        ser.write("4".encode())

        # a.analog_write_value(4)

    elif day == '5':
        print('THURSDAY')
        # a.analog_write_value(5)

    elif day == '6':
        print('FRIDAY')
        # a.analog_write_value(6)

    elif day == '7':
        print('SATURDAY')
        # a.analog_write_value(7)

    elif day == '0':
        print('NOW')
        # a.analog_write_value(0)

    else:
        pass

    # read in analog value from photo resistor
    # readval = a.analog_read(ANALOG_PIN)

    # the default page to display will be our template with our template variables
    # return render_template('index.html', author=author, value=100 * (readval / 1023.))
    return render_template('shadowscape.html')


@app.route('/slider')
def slider():
    return render_template('index.html', **values)


@socketio.on('value changed')
def value_changed(message):
    values[message['who']] = message['data']
    emit('update value', message, broadcast=True)
    print(message)


@socketio.on('day update')
def day_update(message):
    ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

    day_of_week = message['day']
    emit('day become', message, broadcast=True)
    if day_of_week == 'sunday':
        print('SUNDAY')
        # turn on LED on arduino
        # a.digital_write(LED_PIN, 1)
        # a.digital_write_value(1)
        ser.write("1".encode())
        # if we press the turn off button
    elif day_of_week == 'monday':
        print('MONDAY')
        # a.analog_write_value(2)
        ser.write("2".encode())

    elif day_of_week == 'tuesday':
        print('TUESDAY')
        ser.write("3".encode())

    elif day_of_week == 'wednesday':
        print('WEDNESDAY')
        ser.write("4".encode())

    elif day_of_week == 'thursday':
        print('THURSDAY')
        ser.write("5".encode())

        # a.analog_write_value(5)

    elif day_of_week == 'friday':
        print('FRIDAY')
        ser.write("6".encode())

        # a.analog_write_value(6)

    elif day_of_week == 'saturday':
        print('SATURDAY')
        ser.write("7".encode())

        # a.analog_write_value(7)

    elif day_of_week == 'now':
        print('NOW')
        ser.write("0".encode())

        # a.analog_write_value(0)

    print('socket :' + day_of_week)


if __name__ == "__main__":
    # lets launch our web page!
    # do 0.0.0.0 so that we can log into this web page
    # using another computer on the same network later
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')