from threading import Thread

counter = 0

def writer1():
    global counter
    for _ in range(50):
        counter += 1

def writer2():
    global counter
    for _ in range(50):
        counter += 1


t1 = Thread(target=writer1, args=())
t2 = Thread(target=writer2, args=())

t1.start()
t2.start()
t1.join()
t2.join()
print(counter)
