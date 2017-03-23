import time

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

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
@app.route('/')
@app.route('/<day>')
def shadowscape(day=None):
    # if we make a post request on the web page aka press button then do stuff
    if day:

        # if we press the turn on button
        if day == '1':
            print('SUNDAY')
            # turn on LED on arduino
            # a.digital_write(LED_PIN, 1)

        # if we press the turn off button
        elif day == '2':
            print('MONDAY')

            # turn off LED on arduino
            # a.digital_write(LED_PIN, 0)

        elif day == '3':
            print('TUESDAY')

        elif day == '4':
            print('WEDNESDAY')

        elif day == '5':
            print('THURSDAY')

        elif day == '6':
            print('FRIDAY')

        elif day == '7':
            print('SATURDAY')

        elif day == '0':
            print('NOW')

        else:
            pass

    # read in analog value from photo resistor
    # readval = a.analog_read(ANALOG_PIN)

    # the default page to display will be our template with our template variables
    # return render_template('index.html', author=author, value=100 * (readval / 1023.))
    return render_template('shadowscape.html')


@app.route('/slider')
def slider():
    return render_template('index.html')


if __name__ == "__main__":
    # lets launch our web page!
    # do 0.0.0.0 so that we can log into this web page
    # using another computer on the same network later
    app.run(host='0.0.0.0')
