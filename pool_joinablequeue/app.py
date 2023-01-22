import multiprocessing as mp
from multiprocessing import JoinableQueue
import threading
import os
import time
import psutil


def monitor(*args):
    """function run by monitoring thread"""
    line_number = 1
    pool = args[0]
    q = args[1]
    pool_processes = pool._pool
    processes = []
    for process in pool_processes:
        process = psutil.Process(process.pid)
        processes.append(process)

    while True:
        # print("Monitoring...")
        #print(args[0])
        #for process in processes:
        #    print(i, process.pid, process.status())
            #process.terminate()

        time.sleep(1)
        line_number += 1
        if q.empty():
            break


def worker_function(task_queue):
    while True:
        task = task_queue.get()
        if task is None:
            task_queue.task_done()
            break
        print(os.getpid(), task)
        if int(task) > 7:
            try:
                #1/0
                #time.sleep(30)
                pass
            except Exception as e:
                pass
        task_queue.task_done()

def main():
    pid = os.getpid()
    task_queue = JoinableQueue()
    pool = mp.Pool(processes=4, initializer=worker_function, initargs=(task_queue,))

    thread = threading.Thread(target=monitor, args=(pool, task_queue,))
    thread.start()

    # Add tasks to the queue
    for i in range(10000):
        task_queue.put(i)

    # Add None values to the queue to signal the end of tasks to the workers
    for _ in range(4):
        task_queue.put(None)

    task_queue.join()
    print(pid, 'after task_queue.join()')
    pool.close()
    pool.join()
    print(pid, 'after pool.join()')
    thread.join()
    print(pid, "after thread.join()")
    print(pid, 'DONE')


if __name__ == "__main__":
    main()
