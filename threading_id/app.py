import threading

def monitor(a, b):
    print(threading.current_thread().name)
    a.append(99)
    print(id(a), a)
    print(id(b), b)

if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    b = 2
    print(id(a))
    print(id(b))
    thread = threading.Thread(target=monitor, args=(a, b,))
    thread.start()
    thread2 = threading.Thread(target=monitor, args=(a, b,))
    thread2.start()
    thread3 = threading.Thread(target=monitor, args=(a, b,))
    thread3.start()
