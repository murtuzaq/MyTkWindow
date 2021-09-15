import tkinter as tk
import Colorbutton


class MyRightPanel:
    def __init__(self, frame):
        self.frame = frame
        self.__draw_color_canvas()
        self.__draw_button_frame()
        Colorbutton.ColorButton(self.btnFrame, "Red", self.make_circle)
        Colorbutton.ColorButton(self.btnFrame, "Green", self.make_circle)
        Colorbutton.ColorButton(self.btnFrame, "Blue", self.make_circle)
        self.__draw_color_log_text_box()

    def __draw_color_canvas(self):
        self.circleCanvas = tk.Canvas(self.frame, width=100, height=100, background="white")
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

    def __draw_button_frame(self):
        self.btnFrame = tk.Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

    def __draw_color_log_text_box(self):
        self.colorLog = tk.Text(self.frame, width=30, height=10, takefocus=0)
        self.visual_scroll_bar = tk.Scrollbar(self.frame, orient="vertical", command=self.colorLog.yview)
        self.colorLog.configure(yscrollcommand=self.visual_scroll_bar.set)
        self.visual_scroll_bar.grid(row=3, column=1)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)

    def make_circle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert("end", color.capitalize() + "\n")
        self.colorLog.see("end")