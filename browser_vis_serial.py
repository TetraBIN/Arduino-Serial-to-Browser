import serial
import sys
import bottle

ser = serial.Serial('/dev/cu.usbserial-A601EWJ8', 9600)
# print(ser.port)


@bottle.route('/arduino/')
def getArduino():
    #/dev/tty.<port where your arduino is>
    #this will probably not be the same as mine
    #you can find it by entering ls /dev/tty.* to see your
    #ports.  Also in Arduino IDE, go to Tools> Serial Port to
    #see which one you're at
    # ser = serial.Serial('/dev/cu.usbserial-A601EWJ8', 9600)
    # Declear ser before everything happens will prevent delays
    # re-open a serial port may take up to 4 seconds.
    a = ser.readline()
    d = {}
    d['val'] = a
    return d


@bottle.route('/')
def index():
    return open('index.html', 'r')

#These are for debugging, you can uncomment these, and comment out the bottle.run() if you need to debug
#bottle.debug(True)
#bottle.run(reloader = True )
bottle.run()
