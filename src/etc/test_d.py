# coding: utf-8
ip = get_ipython()
ip.editing_mode ='vi'
from main import *
from keysight_api import *
from usb_7270_core import *
import threading as th
scope_output = []
lock_in_output = []
b = th.Barrier(3, timeout=5)
scope_thread = th.Thread(target=run_scope, args=(scope, scope_output, b))
lock_in_thread = th.Thread(target=run_lock_in, args=(lock_in, lock_in_output, b))
scope_thread.start()
lock_in_thread.start()
get_ipython().run_line_magic('save', '-a test_d.py 1-18')
