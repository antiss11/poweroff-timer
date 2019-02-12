import threading
import time

def test(stop_event):
    while not stop_event.wait(1):
        print(1)
        time.sleep(2)
    print("END")

def thread():
    event = threading.Event()
    t = threading.Thread(target=test, args=(event,))
    t.start()
    time.sleep(5)
    event.set()

thread()