import tkinter as tk


class MyLeftPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.__draw_instruction_label()
        self.__draw_steps_label()

    def __draw_instruction_label(self):
        self.__lbl_instruction = tk.Label(self.frame, text="Instructions: ")
        self.__lbl_instruction.grid(row=0, column=0, padx=10, pady=2)

    def __draw_steps_label(self):
        self.__lbl_steps = tk.Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        self.__lbl_steps.grid(row = 1, column = 0, padx = 10, pady = 2)
        