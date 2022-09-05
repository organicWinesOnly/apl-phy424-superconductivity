""" data_field.py 

Class to handle the data for the Teach Spin CMP superconductivity experiment

author: @rhamel
"""
import h5py
import time

BIT_MAP = {0: "X", 1: "Y", 3: "phase", 4: "sensitivity", 5: "Noise"}

class DataField:
    """
    hdf5 object to handle organizing data from CMP project.
    """
    def __init__(self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        self.f = h5py.File("superconductivity_{}.hdf5", "w")
        self._events = self.f.create_group("events")
        self._header = self.f.create_group("header")

    def update_header(self, lock_in_data, scope_data):
        # add lock in data
        for key, arr in lock_in_data:
            self._header.create_data("{}".format(BIT_MAP[key]), data=arr) 

