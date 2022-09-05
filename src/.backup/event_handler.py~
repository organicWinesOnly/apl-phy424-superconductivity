""" event_handler.py
"""
import numpy as np
from collections import deque
from oscilliscope import Oscilliscope
from lockin_7270 import LockIn7270
from data_field import DataField
import threading as th

class EventHandler:
    def __init__(self, scope_id=None):
        self.scope = Oscilliscope()
        self.lock_in = LockIn7270()
        # self.data = DataField()

    def run(self, set_voltage, sample_rate=10000, len_=100000):
        print("Begining data aquisition...")
        scope_output = []
        lock_in_ouput = []
        self.lock_in.set_up()
        self.lock_in.curve_setup(sample_rate, len_)

        events = [th.Event() for i in range(3)]
        lock = th.Lock()  # protect global variables
        curr_fin_voltage = (1000, set_voltage)
        # global _curr_fin_voltage  # (current, set_voltage)
        #final_voltage = set_voltage
        #current_voltage = 1000 #mV

        # initialie threads
        scope_thread = th.Thread(
            target=self.scope.run, 
            args=(
                curr_fin_voltage, 
                events, lock, sample_rate, len_)
            )
        lock_in_thread = th.Thread(
            target=self.lock_in.run, 
            args=(
                curr_fin_voltage, 
                events, lock, sample_rate, len_)
            )

        # Start threads. 
        scope_thread.start()
        lock_in_thread.start()
        # Wait for all threads to finish before returning.
        scope_thread.join()
        lock_in_thread.join()
        print("Run complete.")


    def save_data(self):
        self.data.update_header(self.lock_in.data)
        self.data.update_header(self.lock_in.data)

        

if __name__ == "__main__":
    b = th.Barrier(3, timeout=1)
    event = EventHandler()
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
