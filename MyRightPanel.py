import tkinter as tk


class MyRightPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.__draw_color_canvas()
        self.__draw_button_frame()
        self.__draw_red_button()
        self.__draw_green_button()
        self.__draw_blue_button()
        self.__draw_color_log_text_box()

    def __draw_color_canvas(self):
        self.circleCanvas = tk.Canvas(self.frame, width=100, height=100, background="white")
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

    def __draw_button_frame(self):
        self.btnFrame = tk.Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

    def __draw_red_button(self):
        self.redBtn = tk.Button(self.btnFrame, text="Red", command = lambda: self.__make_circle("red"), background="Red")
        self.redBtn.grid(row=0, column=0, padx=10, pady=2)

    def __draw_green_button(self):
        self.grnBtn = tk.Button(self.btnFrame, text="Green", command = lambda: self.__make_circle("green"), background="Green")
        self.grnBtn.grid(row=0, column=1, padx=10, pady=2)

    def __draw_blue_button(self):
        self.blueBtn = tk.Button(self.btnFrame, text="Blue", command = lambda: self.__make_circle("blue"), background="Blue")
        self.blueBtn.grid(row=0, column=2, padx=10, pady=2)

    def __draw_color_log_text_box(self):
        self.colorLog = tk.Text(self.frame, width=30, height=10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)

    def __make_circle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert(0.0, color.capitalize() + "\n")
