from multiprocessing import JoinableQueue

q = JoinableQueue()
q.put(1)
q.put(2)
q.put(None)


a = 1