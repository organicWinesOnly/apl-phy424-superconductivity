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
    def __init__(self, MANUFACTUR_ID = hex(10893)):
        rm = pyvisa.ResourceManager('')
        dev_name = rm.list_resources("?*::{}?*".format(MANUFACTUR_ID))[0]
        self.dev = rm.open_resource(dev_name)
        self.data = []

    def write(self, cmd:str):
        self.dev.write(cmd)

    def query(self, cmd:str):
        output = self.dev.query(cmd)
        return output

    def save_data(self, len_):
        self.write(":WAVeform:POINts {}".format(len_ + 1))
        output = self.write(":WAVeform:FORMat ASCii")
        output = self.query(":WAVeform:DATA?")
        conv_output = np.array(output.split(',')[1:], dtype=float)
        self.data.extend(conv_output)

    def run(self, curr_fin_voltage, 
            events, lock, 
            sample_rate=10000, len_=100000):
        with lock:
            curr = curr_fin_voltage[0]
            fin = curr_fin_voltage[1]
        print("scope: voltages stored")
        while curr > fin:
            self.dev.write("TIMebase:RANge {}".format(
                len_ * sample_rate / 1e6))
            self.dev.write(":ACQuire:TYPE NORMal")
            events[0].wait()
            print("scope: started run")
            self.dev.write(":DIGItize channel2")
            print("scope: run stopped")
            self.save_data(len_)
            events[1].set()
            print("scope: data saved")
            events[0].clear()
            events[1].clear()
            with lock:
                current_voltage += 100 # self.data[-1] 



# class dewer:
#     def __init__(self):
#         self.scope = oscilliscope()
#         self.lock_in = ametek()
#     
#     def initialize_scope(self):
#         self.osc.write()
# 
# # def set_dvm(osc: oscilliscope):
# #     osc.write(":DVM:ENABle 1")  # enable digital voltmeter (dvm)
# #     osc.write(":DVM:MODE DC")  # set dvm type to DC
# #     osc.write(":DVM:SOURce CHAN1")  # read from CH1 on the scope
# 
# def set_trigger(osc):
#     osc.write(":TRIGger:EDGE:SOURce EXTernal")
# 
# def run_scope(osc, arr, barrier):
#     try:
#         barrier.wait()
#     except:
#         print("Instruments were not syncronized")
#     osc.write(":RUN")
#     time.sleep(1)  # pause for 1 second
#     osc.write(":STOP")
#     osc.write(":WAVeform:POINts 1000")
#     osc.write(":WAVeform:FORMat ASCii")
#     output = osc.query(":WAVeform:DATA?")
#     # output is returned as a string and must be converted to an array
#     data = np.array(output.split(', ')[1:-1])
#     arr.append(data)

# if __name__ == "__main__":
#     MANUFACTUR_ID = hex(10893)
#     rm = pyvisa.ResourceManager('')
#     dev_name = rm.list_resources("?*::{}?*".format(MANUFACTUR_ID))[0]
#     scope = rm.open_resource(dev_name)
# 
#     if not scope:
#         raise ConnectionError("Osciliscope was not found.")
#     else:
#         print("Oscilliscope connected succesfully.")
# 
#     print("Setting DVM settings...")
#     try:
#         set_dvm(scope)
#         print("DVM setting succesful.")
#     except:
#         print("DVM not set.")
# 
#     print("Setting Trigger settings...")
#     try:
#         set_trigger(scope)
#         print("Trigger setting succesful.")
#     except:
#         print("Trigger not set.")
# 
#     print("Run Scope.")
#     try:
#         set_trigger(scope)
#         print("Scope run succesful.")
#     except:
#         print("Scope run unsuccesful.")
