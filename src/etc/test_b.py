# coding: utf-8
import usb.core
usb.core.find()
import pyvisa
rm = pyvisa.ResourceManager('')
rm.list_resources('?*')
ll = usb.core.find()
ll.idVendor
hex(2605)
ll.idProduct
hex(27)
usb.core.find(idVendor='0xa2d', idProduct='0x1b')
usb.core.find(idVendor='0xa2d')
usb.core.find()
usb.core.find(idVendor='0x0a2d')
usb.core.find(idVendor='0x0A2D')
usb.core.find(idVendor=ll.idVendor)
ll.idVendor
usb.core.find(idVendor=ll.idVendor, idProduct=ll.idProduct)
ll.set_configuration()
import array
import numpy as np
def query(dev, ep_in, cmd):
    dev.write(1, cmd)
    r = dev.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
    output = bytes(r[:-4]).decode("utf-8")
    return output
ep_in = lock_in[0].interfaces()[0].endpoints()[1]  # bulk in
ep_out = lock_in[0].interfaces()[0].endpoints()[0]  # bulk out
ep_in = ll[0].interfaces()[0].endpoints()[1]  # bulk in
ep_out = ll[0].interfaces()[0].endpoints()[0]  # bulk out
def query(dev, ep_in, cmd):
    dev.write(1, cmd)
    r = dev.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
    output = bytes(r[:-4]).decode("utf-8")
    return output
    
query(ll, ep_in, "OF.")
ll.write("TD")
ll.write(1, "TD")
ll.write(1, "M")
l = array.array('B')
i = 0
while True:
    try:
        r = ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
        print(i)
        i += 1
    except:
        break
        
l
dev.write(1, "IE 2")
ll.write(1, "IE 2")
ll.write(1, "VMODE 1")
ll.write(1, "AUTOMATIC 1")
ll.write(1, "ASM")
ll.write(1, "X.")
ll.read()
ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
ll.write(1, "X.")
ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
ll.write(1, "X.")
aa = ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
aa
bytes(aa).decode["utf-8"].split("\n")
bytes(aa).decode("utf-8").split("\n")
ll.write(1, "FLOAT 1")
ll.write(1, "LF 0 0")
ll.write(1, "ASM")
ll.write(1, "TC 13")
ll.write(1, "TC 11"))
ll.write(1, "TC 11")
ll.write(1, "AQN")
ll.write(1, "NC")
ll.write(1, "CBD 19")
ll.write(1, "LEN 1000")
ll.write(1, "STR 1000")
ll.write(1, "TD")
ll.write(1, "M")
i = 0
l = array.array('B')
while True:
    try:
        r = ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
        print(i)
        i += 1
    except:
        break
        
data = l.tounicode()
data = l.tolist
data = l.tolist()
data[1]
ll
l[1:100]
l
ll.write(1, "DC. 0")
i = 0
l = array.array('B')
while True:
    try:
        r = ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
        print(i)
        i += 1
    except:
        break
        
data = l.tobytes()
type(data)
dat[1:10]
data[1:10]
data[0]
data[0:100]
x_data = data.split("\n")
output = data.decode("utf-8")
output
x = output.split("\n")
x[0]
x[-1]
x_data = np.array(x[:-1], dtype=float)
import matplotlib.pyplot as plt
ll.write(1, "M")
ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
ll.write(1, "M")
mm = ll.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize).tobytes()
mm
mm[0]
mm[1]
mm.decode("utf-8")
mm.decode("utf-8")[0]
mm.decode("utf-8")[0] == 0
mm.decode("utf-8")[0] == '0'
get_ipython().run_line_magic('save', '-a test_b.py 1-100')
