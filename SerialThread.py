import threading
import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 115200


class SerialThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        s = serial.Serial(PORT, BAUD, timeout=None)
        s.write(str.encode('*00T%'))
        time.sleep(0.2)
        count = 0
        while True:
            if s.inWaiting():
                text = s.readline(s.inWaiting())
                self.queue.put(text)
