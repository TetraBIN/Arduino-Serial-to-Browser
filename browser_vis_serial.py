import serial
import sys
import bottle
from serial.tools import list_ports
# from bottle import Bottle, request, response, run
# bottle.run(reloader=True)
portName = list(list_ports.comports())[-1][0]
# ser = serial.Serial('/dev/cu.usbserial-A601EWJ8', 9600)
ser = serial.Serial(portName, 9600)
# print(ser.port)
# class HTTPResponse(Response, BottleException):
#     def __init__(self, body='', status=None, headers=None, **more_headers):
#         super(HTTPResponse, self).__init__(body, status, headers, **more_headers)
 
#     def apply(self, response):
#         response._status_code = self._status_code
#         response._status_line = self._status_line
#         if self._headers:
#             if response._headers:
#                 response._headers.update(self._headers)
#             else:
#                 response._headers = self._headers
 
#         response._cookies = self._cookies
#         response.body = self.body

@bottle.hook('after_request')
def enable_cors():
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'

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


def cors(func):
    def wrapper(*args, **kwargs):
        bottle.response.set_header("Access-Control-Allow-Origin", "*")
        # bottle.response.set_header("Access-Control-Allow-Origin", "GET, POST, OPTIONS")
        bottle.response.set_headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
        bottle.response.set_header("Access-Control-Allow-Headers", "Origin, Content-Type")
        # skip the function if it is not needed
        if bottle.request.method == 'OPTIONS':
            return

        return func(*args, **kwargs)
    return wrapper


@bottle.route('/')
# @cors
def index():
    return open('index.html', 'r')

# These are for debugging, you can uncomment these, and comment out the bottle.run() if you need to debug
# bottle.debug(True)
# bottle.run(reloader = True )
bottle.run(host='0.0.0.0', port=8080, debug=True)
