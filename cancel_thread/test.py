from multiprocessing import Process, set_start_method
from threading import Thread
from time import sleep
import time
import threading
import ctypes

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event() # The flag used to pause the thread
        self.__flag.set() # Set to True
        self.__running = threading.Event() # Used to stop the thread identification
        self.__running.set() # Set running to True

    def run(self):
        try:
             while self.__running.is_set():
                self.__flag.wait() # return immediately when it is True, block until the internal flag is True when it is False
                print( time.time())
                time.sleep(1)
        finally:
            print("finally")

    def pause(self):
        #1/0
        self.__flag.clear() # Set to False to block the thread
        

    def resume(self):
        self.__flag.set() # Set to True, let the thread stop blocking

    def stop(self):
        self.__flag.set() # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear() # Set to False

    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id


    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
        #if True:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
      






def do_process():
    pass

def do_thread():
    for i in range(5):
        a = 1
        print("t")
        sleep(1)
    print("done t")

def exc(self):
    1/0


if __name__ == '__main__':
    set_start_method("spawn")
    Thread.exc = exc
    #t = Thread(target=do_thread)
    #t.start()
    #t.exc()
    job = Job(target=do_thread)
    job.start()
    sleep(1)
    #job.pause()
    job.raise_exception()
    #t.setDaemon(True)
    print("done")
