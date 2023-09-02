# Python program raising
# exceptions in a python
# thread
 
import threading
import ctypes
import time


class ThreadWithException(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
             
    def run(self):
        # target function of the thread class
        try:
            # raise_exception cannot kill a sleeping thread.
            # time.sleep(500)

            # Terminating a thread using raise_exception does
            # not terminate the child thread.
            t2 = threading.Thread(target=do_thread2)
            t2.start()

            while True:
                print('running ' + self.name)
                time.sleep(1)
        finally:
            print('Thread 1 ended')
          
    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
              ctypes.py_object(SystemExit))
        print(res)
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

def do_thread2():
    while True:
        print("thread2")
        time.sleep(1)


t1 = ThreadWithException('Thread 1')
t1.start()
time.sleep(2)
t1.raise_exception()
t1.join()
