import threading
import time

def myThread1():
    print("Started thread ", threading.current_thread())
    
    time.sleep(1)
    
    print("Ending thread ", threading.current_thread())

def myThread2(value):
    print("Started thread ", threading.current_thread())
    
    print("Value=", value)
    time.sleep(1)
    
    print("Ending thread ", threading.current_thread())

if __name__ == "__main__":
    print("Starting threads...")
    
    # create thread 1, no arguments
    t1 = threading.Thread(name="first", target=myThread1)
    
    # create thread 2, 1 argument
    t2 = threading.Thread(name="second", target=myThread2, args=("hello",))
    
    # start threads
    t1.start()
    t2.start()
    
    # wait for threads, no timeout
    t1.join()
    t2.join()
    
    print("Done")
