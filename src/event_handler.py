""" event_handler.py
"""
import numpy as np
from oscilliscope import Oscilliscope
from lockin_7270 import LockIn7270
import threading as th

class EventHandler:
    """ This class handles the data aquisition for the condensed matter physics
        - superconductivity experiment.


       Public Methods
       --------------
       run(...) - aquires data from the system up to a set transdiode voltage
           reading. 

       Public Attributes 
       --------------
       scope - Instance usb interface with Keysight Digitial Oscilliscope. Powered 
           by pyvisa. 
       lock_in - Instance usb interface with AMETEK Lock In Amplifier. Powered by pyusb.
    """
    def __init__(self, scope_id=None):
        """ Initalize class. 

            Paramaters
            ----------
            scope_id : int
                Oscilliscope manufactur id. 
        """
        if not scope_id:
            self.scope = Oscilliscope()
        else:
            self.scope = Oscilliscope(sope_id)
        else: 
        self.lock_in = LockIn7270()

    def run(self, set_voltage, sample_rate=100000):
        """ Run data aquisition.

            The system begins data aquisition at the given <sample_rate>
            starting from a cold point of (1 V) to the set point, <set_voltage>,
            which is a readout of the transdiode. 

            Paramaters
            ----------
            set_voltage: float
                When the oscilliscope reads a voltage value lower than this the
                aquision stops. Paramter is in volts. 
            sample_rate: int
                The sample rate in microseconds. The minimum value is 1000 which
                is equivalent to 1ms. Default: 100000 microseconds = 100 ms.
        """
        len_ = 300  # data buffer size
        print("Begining data aquisition...")
        self.lock_in.set_up()
        self.lock_in.curve_setup(sample_rate, len_)

        events = [th.Event() for i in range(3)]
        barrier = th.Barrier(2)
        lock = th.Lock()  # protect global variables
        curr_fin_voltage = [1, set_voltage]

        # initialie threads
        scope_thread = th.Thread(
            target=self.scope.run, 
            args=(
                curr_fin_voltage, 5,
                events, lock, barrier, sample_rate, len_)
            )
        lock_in_thread = th.Thread(
            target=self.lock_in.run, 
            args=(
                curr_fin_voltage, 
                events, lock, barrier, sample_rate, len_)
            )

        # Start threads. 
        scope_thread.start()
        lock_in_thread.start()
        # Wait for all threads to finish before returning.
        scope_thread.join()
        lock_in_thread.join()
        print("Run complete.")

    # def save_data(self):
    #     self.data.update_header(self.lock_in.data)
    #     self.data.update_header(self.lock_in.data)
