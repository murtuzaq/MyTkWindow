import threading
import serial
import time

class SerialThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        self.counter = 0
        while True:
            time.sleep(1.0)
            print("run time = ", self.counter)
            self.counter += 1

    def dont_run(self):
        s = serial.Serial('/dev/ttyS0', 115200)
        s.write(str.encode('*00T%'))
        time.sleep(0.2)
        while True:
            if s.inWaiting():
                text = s.readline(s.inWaiting())
                self.queue.put(text)

