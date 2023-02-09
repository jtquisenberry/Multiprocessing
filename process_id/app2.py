from multiprocessing import Process, Manager
import pandas as pd
import numpy as np

def monitor(a, b, c, v):
    xxx = v[0]
    #print(type(xxx))
    xxx[0, 0] += 1
    print(a, xxx)
    v[0] = xxx
    print(a, v[0])


if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    b = 2

    arr = np.ones([3, 3])

    mgr = Manager()
    ns = mgr.Namespace()
    ns.arr = arr
    v = mgr.list([arr,])

    #print(id(a))
    #print(id(b))
    print('v-main', id(v))

    process = Process(target=monitor, args=("proc1", arr, ns, v))
    process.start()
    process2 = Process(target=monitor, args=("proc2", arr, ns, v))
    process2.start()
    process3 = Process(target=monitor, args=("proc3", arr, ns, v))
    process3.start()

    process.join(), process2.join(), process3.join()
