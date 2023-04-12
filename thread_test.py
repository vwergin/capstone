from threading import Thread
import time

first = 1
def func1():
    global first
    if first==1:
        print("1")
    else:
        fun = func3()
    first = first + 1
def func2():
    print("2")

def func3():
    print("3")

test = True
num = 1
while test:
    if num <6:
        Thread(target = func1).start()
        Thread(target = func2).start()
        time.sleep(2)
    else:
        break
    print("num",num)
    num = num +1
