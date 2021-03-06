from threading import Thread
from time import sleep
'''
Python  process waits for all non-daemon threads to finish execution.
It does not take care of daemon threads.
Once all non daemon threads have finished execution,
Python will exit even if daemon threads are still under excution.
'''
class MyThread(Thread):
    def __init__(self,name,delay):
        Thread.__init__(self)
        self.setName(name)
        self.delay=delay
    def run(self):
        for i in range(1,11):
            print(str(i)+self.getName())
            sleep(self.delay)

t1=MyThread("Sachin",1.5)
t2=MyThread("Saurav",1)
t3=MyThread("Rahul",0.5)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
t3.start()
