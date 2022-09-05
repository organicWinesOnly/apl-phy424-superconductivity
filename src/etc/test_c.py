# coding: utf-8
from main import *
from main import *
from usb_7270_core import *
take_data(lock_in, ep_in)
query(lock_in, ep_in, "M")
lock_in.write(1, "M")
lock_in.write(1, "M")
r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
r
r.tobytes()
r.tobytes().decode("utf-8")
r.tobytes().decode("utf-8")[0]
x = read_curve(lock_in, ep_in, 0)
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = dev.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
out = l.tobytes().decode("utf-8")
out[-5:]
out[-5]
out
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = dev.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
l
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
l
out = l.tobytes().decode("utf-8")
out
daata = out.split("\n")
daata[-1]
daata[0]
np.array(daata[:-1])
x = np.array(daata[:-1], dtype=np.float64)
x = np.frombuffer(out, dtype=np.float64)
x = np.frombuffer(l, dtype=np.float64)
x
x = np.frombuffer(l.tobytes(), dtype=np.float64)
x
x = np.frombuffer(l.tobytes(), dtype=np.float32)
x
l[:100]
x = np.frombuffer(l.tobytes(), dtype=float)
x
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
type(l)
x = np.frombuffer(l)
x
lock_in.write(1, "DC. 0")
l = array.array('f')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
x = np.frombuffer(l)
x
l
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except:
        break
        
x = np.frombuffer(l, dtype=uint8)
x = np.frombuffer(l, dtype=uint)
l
l.tobytes().decode("ascii")
x = np.array(l.tobytes().decode("ascii").split("\n"))
x
x = np.array(l.tobytes().decode("ascii").split("\n"), dtype=float)
x = np.array(l.tobytes().decode("base64").split("\n"), dtype=float)
x = np.array(bytes(l).split("\n"), dtype=float)
x = np.array(bytes(l).decode("utf-8").split("\n"), dtype=float)
l
l.tobytes().decode("utf-8")
out = l.tobytes().decode("utf-8").split("\n")
out
lock_in.write(1, "DC. 0")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except Exception as e:
        print(e)
        break
        
l
lock_in.write(1, "DC. 0")
print("data stored")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except Exception as e:
        print(e)
        break
        
lock_in.write(1, "DC. 0")
print("data stored")
l = array.array('B')
while True:
    try:
        r = lock_in.read(ep_in.bEndpointAddress, ep_in.wMaxPacketSize)
        l = l + r
    except Exception as e:
        print(e)
        l = l + r
        break
    
x = np.array(l.tobytes().decode("utf-8").split("\n"), dtype=float)
x = np.array(l.tobytes().decode("utf-8").split("\n")[:-1], dtype=float)
l.tobytes().decode("utf-8").split("\n")
x = np.array(l.tobytes().decode("utf-8").split("\n")[:-3], dtype=float)
import matplotlib.pyplot as plt
plt.plot(x)
plt.show()
get_ipython().run_line_magic('save', '-a test_c.py 1-100')
