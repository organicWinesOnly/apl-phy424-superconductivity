import time
import numpy as np
import array
import usb.core

###############################################################################
# Lock in class
###############################################################################
SETUP_CMDS = {
    "REMODE": 0, "VMODE": 3, "IE": 0,
    "DCCOUPLE": 0, "FLOAT": 1, "TC": 12,
    "FET": 0}


class LockIn7270:
    """ Instance of an Ametek 7270 lock in amplifier


       Public Methods
       --------------
       query(..) - write and read commands to device
       setup(..) - update device settings
       curve_setup(..) - update device settings for new curve measurement
       run(..) - complete curve measurements
       read_curve(..) - read curve data for a single attribute into data buffer
       read_all_curves - read all curves into data buffer

       Public Attributes
       ----------------
       dev - lock in device
       data - dictionary of stored data measurements
       ep_in/_out - location of in and out usb endpoints respectively
       
        # dev.write(1, "REFMODE 0")  # single reference mode
        # dev.write(1, "IE 0")  # internal reference
        # dev.write(1, "VMODE 3")  # A-B differential mode
        # dev.write(1, "DCCOUPLE 0")  # AC coupling
        # dev.write(1, "FLOAT 1")  # floating ground
        # # dev.write(1, "AUTOMATIC 1")  # automatic AC gain setting
        # # dev.write(1, "ASM")  # auto sensitivity mode
        # dev.write(1, "TC 12")  # 100 ms time constant
        # dev.write(1, "FET 0")  # bipolar device
    """
    def __init__(self, id_vendor=2605, id_product=27, cmds=SETUP_CMDS):
        """ Initialize class.
         
            Paramaters
            ----------
            id_vendor : int 
                ...
            id_product : int 
                ...
            cmds : dict
                ...
        """
        self.dev = usb.core.find(idVendor=id_vendor, idProduct=id_product)
        self.dev.set_configuration()
        self.paramaters = cmds
        # in and out endpoints respectively
        self.ep_in = self.dev[0].interfaces()[0].endpoints()[1]  # bulk in
        self.ep_out = self.dev[0].interfaces()[0].endpoints()[0]  # bulk out
        self.data = {0: [], 1: [], 3: [], 4: [], 5: []}  

    def query(self, cmd, silent=False):
        """ Write and read a command to the lock in instrument.
            
            Paramaters
            ----------
            cmd : str
                The command.
            silent : bool
                Wheter the read message should be printed to the screen.
        """
        self.dev.write(1, cmd)
        try:
            output = self.dev.read(
                self.ep_in.bEndpointAddress, 
                self.ep_in.wMaxPacketSize)
            if !silent:
                print(output.tobytes().decode("utf-8"))
        except:
            if !silent:
                print('')

    def set_up(self):
        """ Write settings based on the parameter attribute. """
        for cmd, value in self.paramaters.items():
            self.dev.write(1, "{} {}".format(cmd, value))

    def curve_setup(self, sample_rate=10000, len_=100000):
        """ Initialize curve collection settings of the device.

            Paramaters
            ----------
            sample_rate : int
                Time steps between measurements in microseconds (minimum: 1 - in fast
                mode; 1000 standard mode)
            len_ : int
                Number of measuremnts to store (max = 100,000)
        """
        self.query("NC")  # clear curve buffer
        self.query("CMODE 0")  # set curve aquistion to fast mode
        self.query("CBD 59")  # store X,Y, phase, sensitivity, Noise
        self.query("LEN {}".format(len_))
        # max len value is 100,000
        self.query("STR {}".format(sample_rate))  # store data every 10 ms [in micro-s]
        # 10 Hz * 1000000 = 100
        self.query("REFP 0")  # set phase to 0

    def read_curve(self, bit_):
        """ Read and save curve data for the specified <bit_> value. 
            
            Read curve data, convert data to floating point numbers, and store
            results in data attribute at corresponding location.
            
            Paramaters
            ----------
            bit_ : int
                ....
        """
        output = array.array('B')
        self.dev.write(1, "DCB {}".format(bit_))
        while True:
            try:
                r = self.dev.read(self.ep_in.bEndpointAddress, self.ep_in.wMaxPacketSize)
                output.extend(r)
            except:
                break

        data = []
        # the len(output)-3 converts all the bytes except the null byte which
        # takes up the last 3 positions of the output array 
        for i in range(0, len(output)-3, 2):
            byte_str = output[i:i+2].tobytes()
            # see page 6-31 under DCB command for details on the bytes outputted
            value = int.from_bytes(byte_str, byteorder="big", signed=True)
            data.append(value)
        self.data[bit_].extend(data)

    def read_all_curves(self):
        """ Save all curves stored in device buffer to computer.
        """
        for i in self.data.keys():
            self.read_curve(i)


    def run(self, curr_fin_voltage,
            events, lock, 
            sample_rate=10000, len_=1000000):
        """ Run curve aquistion.
        """
        print("Lock in running.")
        with lock:
            curr = curr_fin_voltage[0]
            fin = curr_fin_voltage[1]
        while curr > fin:
            print("Lock in: voltages saved")
            self.curve_setup(sample_rate, len_)
            print("Lock in: curve setup")
            events[0].set()
            self.dev.write(1, "TD")
            print("Lock in: taking data")
            time.sleep(len_ * sample_rate / 1e6 + 1e-5)
            print("Lock in: saving data")
            self.read_all_curves()
            events[1].wait()
            print("Lock in: data saved")

