import os
from ctypes import *

path = os.path.join(os.path.dirname(__file__), 'lib.dll')
myLib = cdll.LoadLibrary(path)
myLib.interpolateNewton.argtypes = (POINTER(c_float), POINTER(c_float), c_int, c_float)
myLib.interpolateNewton.restype = c_float


def calculate(x, f, val):
    n = len(x)
    c_arr = n * c_float
    return myLib.interpolateNewton(c_arr(*x), c_arr(*f), c_int(n), c_float(val))
