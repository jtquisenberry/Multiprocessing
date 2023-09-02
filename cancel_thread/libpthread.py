# https://code.activestate.com/lists/python-ideas/56383

import time
import threading
import ctypes

def handler():
    # blocked thread handler
    time.sleep(1000)

t = threading.Thread(name='bar', target=handler)
libpt = ctypes.cdll.LoadLibrary("libpthread.so.0")

t.start()
libpt.pthread_cancel(ctypes.c_ulong(t.ident))
# This is nasty cleaning of internal python structures
del threading._active[t.ident]
