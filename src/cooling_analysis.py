import numpy as np
import matplotlib.pyplot as plt

time, ln2_mv, bp_mv, ln2_added = np.loadtxt("data/cooling_measurements.txt",
        unpack=True, dtype=int)

t_slice = []
add_ = []
for i in range(len(ln2_added)):
    if ln2_added[i] > 0:
        t_slice.append(time[i])
        add_.append(ln2_mv[i])
plt.figure()
plt.plot(time, ln2_mv, label="Voltage measurements on resevoir")
plt.plot(time, bp_mv, label="Voltage measurements on baseplate")
plt.scatter(t_slice, add_, marker='D', color='red', label="Coolant added")
plt.xlabel("Time [Minutes]")
plt.ylabel("Voltage mV")
plt.title("Cooling timestamps")
plt.legend()
plt.show()

