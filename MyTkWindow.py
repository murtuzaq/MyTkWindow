import tkinter as tk
import MyLeftPanel
import MyRightPanel
import queue
import SerialThread

class MyTkWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.__draw_base_window()
        self.__draw_left_frame()
        self.__draw_right_frame()

        self.queue = queue.Queue()
        serial_thread = SerialThread.SerialThread(self.queue)
        serial_thread.start()


    def start(self):
        self.root.mainloop()

    def __draw_base_window(self):
        self.root.title("Window Title")
        self.root.config(background="White")

    def __draw_left_frame(self):
        left_frame = tk.Frame(self.root, width=200, height=600)
        left_frame.grid(row=0, column=0, padx=10, pady=2)
        MyLeftPanel.MyLeftPanel(left_frame)

    def __draw_right_frame(self):
        right_frame = tk.Frame(self.root, width=200, height=300)
        right_frame.grid(row=0, column=1, padx=10, pady=2)
        MyRightPanel.MyRightPanel(right_frame)
