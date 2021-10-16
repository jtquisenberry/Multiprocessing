import multiprocessing


tasks = multiprocessing.JoinableQueue(maxsize=2)
tasks.put(0)
tasks.put(1)

# tasks.empty() can be made True with repeated calls to
# tasks._recv_bytes()
# _recv_bytes calls _winapi.ReadFile
# It may not be the case that _recv_bytes works faster than
# tasks.get()
task_value = tasks._recv_bytes()


b = 1

tasks.get()
tasks.close()


a = 1
