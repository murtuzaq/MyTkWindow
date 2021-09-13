import tkinter as tk
from PIL import Image, ImageTk


class MyLeftPanel:
    def __init__(self, frame):
        self.frame = frame
        self.__draw_instruction_label()
        self.__draw_steps_label()

    def __draw_instruction_label(self):
        lbl_instruction = tk.Label(self.frame, text="Instructions: ")
        lbl_instruction.grid(row=0, column=0, padx=10, pady=2)

    def __draw_steps_label(self):
        lbl_steps = tk.Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        lbl_steps.grid(row=1, column=0, padx=10, pady=2)
