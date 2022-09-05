""" temp_calibration.py

    Temperature Calibration function.
"""
import numpy as np
from scipy import optimize

"""
2 pt Calibration ------------
[ 7.51494326e+00 -4.22151611e-03]
3 pt Calibration ------------
[ 9.08295001e+00 -6.70508037e-03]
"""
# MEAS1 = (297.3, 8.77)
# MEAS2 = (77, 7.84)

"""  LN2 transdiode
2 pt Calibration ------------
[1186.10562103    2.52085222]
3 pt Calibration ------------
[1187.67374527    2.51837018]
"""
MEAS1 = (297.6, 435.9)
MEAS2 = (77, 992)  # (K, mV)


temp_data = [MEAS1[0], MEAS2[0]]
voltage_data = [MEAS1[1], MEAS2[1]]

def calibration2_ln2(temp):
    """ Two point calibration.
    """
    return 1186.10562 - 2.5208 * temp

def calibration2(temp, c1, c2):
    """ Two point calibration.
    """
    return c1 - c2 * temp

def calibration3(temp, d1, d2):
    """ Two point calibration.
    """
    return d1 - d2 * temp - 0.405 * np.log(temp)

popt2, _ = optimize.curve_fit(calibration2, temp_data, voltage_data)
popt3, _ = optimize.curve_fit(calibration3, temp_data, voltage_data)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    test_temp = np.linspace(temp_data[1], temp_data[0], 1000)
    print("--------Calibration Results------------")
    print("2 pt Calibration ------------")
    print(popt2)
    print("3 pt Calibration ------------")
    print(popt3)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(test_temp, calibration2(test_temp, *popt2))
    ax1.set_title("2 pt calibration")
    ax2.plot(test_temp, calibration3(test_temp, *popt3))
    ax2.set_title("3 pt calibration")
    plt.show()
    
