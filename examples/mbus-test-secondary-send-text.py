#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Copyright (C) 2012, Robert Johansson <rob@raditex.nu>, Raditex Control AB
# All rights reserved.
# ------------------------------------------------------------------------------

"""
mbus test: send custom text to secondary address
Only works with jouzer/python-mbus fork, need libmbus and python-mbus. If you reinstall,
you probably need to sudo make clean, sudo make install in libmbus,
and then sudo python3 setup.py install again in python-mbus
You can check that the .so file has the new function mbus-send-custom-text with nm -D /path/to/libmbus.so , obviously change your dir there
Also change the select_secondary_address to your Elvaco CMa10 device and device to your rs232 device (or whatever you use)
"""

from mbus.MBus import MBus

debug = True
#address = 0
address = 0xFD #secondary


#mbus = MBus(host="mbus-gw1", port=8888)
mbus = MBus(device="/dev/ttyUSB0", libpath="/usr/local/lib/libmbus.so")

if debug:
    print("mbus = " + str(mbus))

mbus.connect()

if debug:
    print("mbus = " + str(mbus))

mbus.serial_set_baudrate(2400)
ret = mbus.select_secondary_address("24134667FFFFFFFF")

#res = mbus.send_ping_frame(0xFD, 1)
#print(res)
#res = mbus.send_ping_frame(0, 1)
#print(res)
# fairly sure these pings not needed
text = "PYTHONpython"
mbus.send_custom_text(address, text)

try:
    reply = mbus.recv_frame()
    mbus.frame_free(reply)
except Exception as e:
    if "libmbus.mbus_recv_frame failed" in str(e):
        reply = "Device did not respond."
    else:
        reply = f"Unexpected error: {e}"

if debug:
    print("reply =", reply)

mbus.disconnect()
