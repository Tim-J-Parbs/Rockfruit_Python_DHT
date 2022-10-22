# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from . import common
from . import Radxa_Zero_gpiod_Driver as driver
BOARD = [None, 1,  2,3,4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27, 28,29,30,31,32,33,34,35,36,37,38,39,40]
BCM =   [27,  28,  3,5,7,29,31,26,24,21,19,23,32,33, 8,10,36,11,12,35,38,40,15,16,18,22,37,13]

#BOARD =[None,    1,      2,   3,   4, 5,    6, 7, 8,    9,10,11,12,13,   14,   15,16,  17,18,19,   20,21,22,23,24,  25,
#          26,27, 28,  29,  30,  31,32,  33,  34,35,36,37,38,  39,40]
LINE =  [None, None,   None,  63,None,64, None, 3, 0, None, 1, 2,74,76, None, None,75,None,73,20, None,21,48,23,22,None,
         None, 3,  2,None,None,None, 4,None,None, 8,24, 9,10,None,11]
def boardpin2line(pin):
    linepin = LINE[pin]
    return linepin

def read(sensor, pin):
    # Validate pin is a valid GPIO.
    pin = boardpin2line(int(pin))
    if pin is None or int(pin) < 0 or int(pin) > 80:
        raise ValueError('Pin must be a valid GPIO number 0 to 31, Excluding weirdo pins.')
    # Get a reading from C driver code.
    print('accessing driver')
    result, humidity, temp = driver.read(sensor, int(pin))
    if result in common.TRANSIENT_ERRORS:
        # Signal no result could be obtained, but the caller can retry.
        return (None, None)
    elif result == common.DHT_ERROR_GPIO:
        raise RuntimeError('Error accessing GPIO.')
    elif result != common.DHT_SUCCESS:
        # Some kind of error occured.
        raise RuntimeError('Error calling DHT test driver read: {0}'.format(result))
    return (humidity, temp)
