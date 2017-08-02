# coding: UTF-8

import serial
from xbee import ZigBee
serial_port = serial.Serial('/dev/tty.usbserial-AH016V4K', 9600)
zb = ZigBee(serial_port)

        # Send AT packet
# zb.send('at', frame_id='A'.encode("UTF-8"), command='DH'.encode("UTF-8"))
#
# # Wait for response
# response = zb.wait_read_frame()
# print(response)

# # Send AT packet
zb.send('tx', frame_id='B'.encode("UTF-8"),
dest_addr=b'\xFF\xFE',
 dest_addr_long='\x00\x13\xA2\x00\x40\xA8\xB8\x94',
 data='test'.encode("UTF-8"))
# # Wait for response
response = zb.wait_read_frame()
print(response)
#
#
# zb.send('at', frame_id='C', command='MY')
# response = zb.wait_read_frame()
# print(response)
#
serial_port.close()
