import tkinter as tk
import MyLeftPanel
import MyRightPanel

class MyTkWindow:
    def __init__(self):
        self.__draw_base_window()
        self.__draw_left_frame()
        self.__draw_right_frame()

    def start(self):
        self.root.mainloop()

    def __draw_base_window(self):
        self.root = tk.Tk()
        self.root.title("Window Title")
        self.root.config(background = "White")

    def __draw_left_frame(self):
        self.left_frame = tk.Frame(self.root, width = 200, height = 600)
        self.left_frame.grid(row = 0, column = 0, padx = 10, pady = 2)
        MyLeftPanel.MyLeftPanel(self.root, self.left_frame)

    def __draw_right_frame(self):
        self.right_frame = tk.Frame(self.root, width=200, height=300)
        self.right_frame.grid(row=0, column=1, padx = 10, pady = 2)
        MyRightPanel.MyRightPanel(self.root, self.right_frame)
