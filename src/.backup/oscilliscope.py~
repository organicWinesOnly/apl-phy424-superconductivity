""" Library of functions to connect to keysight DSO1202G oscilliscope via usb
remote control.

author: @rhamel
"""


""" attributes specific to DSOX1202G

if using a different scope:
    1. Find the sope using pyvisa.ResourceManager()
    2. scope will have attributes 'manufactur_id' and 'model_code' which will
    need to be converted to hexidecimal using the hex() function.
"""
import pyvisa
import time
import numpy as np

class Oscilliscope:
    """ Instance of Keysight 1202G Oscilisope.

        NOTE: For this to cass to work it is assumed that the transdiode analog
        connection is connected to CH1 of the osciliscope.

        Public Methods
        --------------
        write(..) - Write commands to device.
        query(..) - Write command to device and return device response (only
                    works with commands ending with a question mark '?').
        run(..) - Run data aquistion.
        save_data - Move data aquired on device and save to computer. 

        Public Attributes
        -----------------
        dev - device
        data - voltage readings
    """
    def __init__(self, MANUFACTUR_ID = hex(10893)):
        rm = pyvisa.ResourceManager('')
        dev_name = rm.list_resources("?*::{}?*".format(MANUFACTUR_ID))[0]
        self.dev = rm.open_resource(dev_name)
        self.data = []

    def write(self, cmd:str):
        """ Write a command to the osiliscope.
            
            Paramaters
            ----------
            cmd : str
                The command.
        """
        self.dev.write(cmd)

    def query(self, cmd:str):
        """ Write and read a command to the osciliscope.
            
            Paramaters
            ----------
            cmd : str
                The command.
        """
        output = self.dev.query(cmd)
        return output

    def save_data(self, len_):
        self.write(":WAVeform:POINts {}".format(len_ + 2))
        self.write(":WAVeform:FORMat ASCii")
        output = self.query(":WAVeform:DATA?")
        conv_output = np.array(output.split(',')[1:], dtype=float)
        self.data.extend(conv_output)

    def _initialize_run(self, n_average, run_time):
        self.dev.write("TIMebase:MODE MAIN")
        self.dev.write("TIMebase:RANge {}".format(
            run_time / n_average))
        self.dev.write(":ACQuire:TYPE AVERage")
        self.dev.write(":ACQuire:COUNt {}".format(n_average))
        self.dev.write(":ACQuire:TYPE NORMal")
        self.dev.write(":CHANnel2:OFFSet 650mV")
        self.dev.write(":CHANnel2:RANge 600mV")

    def run(self, curr_fin_voltage, n_average,
            events, lock, barrier,
            sample_rate=10000, len_=100000):
        run_time = len_ * sample_rate * 1e-6 + 1e-2
        self._initialize_run(n_average, run_time)
        with lock:
            curr = curr_fin_voltage[0]
            fin = curr_fin_voltage[1]
        while curr > fin:
            events[0].wait()
            self.dev.write(":DIGItize channel1")
            time.sleep(run_time)
            self.save_data(len_)
            events[1].wait()
            events[0].clear()
            with lock:
                curr_fin_voltage[0] = self.data[-1] 
                curr = curr_fin_voltage[0]
            barrier.wait()
            barrier.reset()
