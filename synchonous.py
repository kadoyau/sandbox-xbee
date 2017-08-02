# coding: UTF-8

import serial
from xbee import ZigBee
serial_port = serial.Serial('/dev/tty.usbserial-AH016V4K', 9600)
zb = ZigBee(serial_port)
while True:
    try:
        print(zb.wait_read_frame())
    except KeyboardInterrupt:
        break
serial_port.close()
