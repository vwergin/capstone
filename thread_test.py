from threading import Thread
import time

test = True
first = 1
def func1():
    global first
    global test
    if first==1:
        print("1")
    else:
        func3()
    first = first + 1
    test = False
    print("test1", test)
def func2():
    print("2")

def func3():
    print("3")

num = 1
while test:
    print("test2", test)
    if num <6:
        Thread(target = func1).start()
        Thread(target = func2).start()
        time.sleep(2)
    else:
        break
    print("num",num)
    num = num +1
