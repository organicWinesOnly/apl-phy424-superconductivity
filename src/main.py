import pyvisa
import usb.util
import numpy as np
import array
import usb.core


print("-------- Connecting Instruments --------")
# Connect instruments
ID_VENDOR = 2605  # product specific details of the lock_in amplifier used
ID_PRODUCT = 27
lock_in = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT)
lock_in.set_configuration()
ep_in = lock_in[0].interfaces()[0].endpoints()[1]  # bulk in
ep_out = lock_in[0].interfaces()[0].endpoints()[0]  # bulk out

if not lock_in:
    raise ConnectionError("Lock-in was not found.")
else:
    print("Lock-in connected succesfully.")

MANUFACTUR_ID = hex(10893)
rm = pyvisa.ResourceManager('')
dev_name = rm.list_resources("?*::{}?*".format(MANUFACTUR_ID))[0]
scope = rm.open_resource(dev_name)


if not scope:
    raise ConnectionError("Osciliscope was not found.")
else:
    print("Oscilliscope connected succesfully.")

if __name__ == "__main__":
    from usb_7270_core import *
    from keysight_api import *
    import threading as th
    import matplotlib.pyplot as plt

    b = th.Barrier(3, timeout=1)
    scope_output = []
    lock_in_ouput = []
    print("Collecting data...")

    # Set up scope
    set_dvm(scope)
    set_trigger(scope)
    scope_thread = th.Thread(target=run_scope, args=(scope, scope_output, b))
    scope_thread.start()

    # set up lock-in
    lock_in_thread = th.Thread(target=run_lock_in, args=(lock_in, lock_in_output,
        b))
    lock_in_thread.start()
    b.wait()
    
    # plot