Python DHT Sensor Library with support for libmraa and libgpiod
=======================

Python library to read the DHT series of humidity and temperature sensors on a variety of boards. 
In the original version by Tony DiCola, Raspberry Pi Beaglebone Black boards were supported. 
This version adds support for Radxa boards, using librmaa or libgpiod libraries.

Currently the library is tested with Python 3.9. The added support is only tested with a Radxa Zero board, 
but should work fine on comparable devices.

Installing
----------

### Dependencies

For all platforms make sure your system is
able to compile and download Python extensions with **pip**:

You can ensure your
system is ready by running one or two of the following sets of commands:

Python 3:

````sh
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
````

### Radxa board specifics
If you are using a Radxa board, confirm you have either ```libmraa``` or ```libgpiod``` installed. ```libmraa``` comes preinstalled on all 
current OS versions (else, installation depends on your board and is found in the Radxa wiki.)

```libgpiod``` should be the preferred option, as it seems much faster and more stable. Installation is straightforward:
```sh
sudo apt update
sudo apt install gpiod -y
```
Note that ```libgpiod``` uses a different pin numbering scheme. This driver has built-in conversion, so the same pin numbering
scheme (#1 to #40) can be used for both ```libmraa``` and ```libgpiod```. This was only tested on Radxa Zero, if you want to use 
```libgpiod``` and specify the line number directly, use the optional argument ```numbering``` like:
```sh
import Rockfruit_DHT as driver
temp, humidity = driver.read(driver.DHT22, linepin, numbering='line')
```

### Compile and install from the repository

First download the library source code, unzip the
archive, and execute:

```sh
cd Rockfruit_Python_DHT
sudo python3 setup.py install
```
For Radxa boards, the installer first tries to build against ```libgpiod```. If you want to use ```libmraa```, append ```--force-libmraa``` to the install line.


Author
------

Adafruit invests time and resources providing this open source code, please
support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries, modified by Tim Parbs for Radxa boards.

MIT license, all text above must be included in any redistribution
