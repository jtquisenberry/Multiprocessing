from multiprocessing import Process, Manager
import os

def monitor(a, b):
    
    a.append(99)
    print(id(a), a)
    print(id(b), b)

if __name__ == '__main__':

    manager = Manager()

    aa = [1, 2, 3, 4, 5]
    b = 2

    a = manager.list([1, 2, 3, 3, 3])
    print(id(a))
    print(id(b))
    process = Process(target=monitor, args=(a, b,))
    process.start()
    process2 = Process(target=monitor, args=(a, b,))
    process2.start()
    process3 = Process(target=monitor, args=(a, b,))
    process3.start()

    process.join(), process2.join(), process3.join()
