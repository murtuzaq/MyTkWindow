import tkinter as tk
from PIL import Image, ImageTk


class MyLeftPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        self.__draw_instruction_label()
        self.__draw_steps_label()
        #self.__draw_image()

    def __draw_instruction_label(self):
        self.__lbl_instruction = tk.Label(self.frame, text="Instructions: ")
        self.__lbl_instruction.grid(row=0, column=0, padx=10, pady=2)

    def __draw_steps_label(self):
        self.__lbl_steps = tk.Label(self.frame, text="1\n2\n2\n3\n4\n5\n6\n7\n8\n9\n")
        self.__lbl_steps.grid(row=1, column=0, padx=10, pady=2)

    def __draw_image(self):
        # self.__example_image = Image.open("image.jpg")
        # self.__example_image.show()
        # self.__lbl_image = tk.Label(self.frame, image=self.__example_image)
        # self.__lbl_image.grid(row=2, column=0, padx=10, pady=2)
        self.image = Image.open('image.jpg')
        self.python_image = ImageTk.PhotoImage(self.image)
        #self.__photo_image = tk.PhotoImage(file="python_logo.png")
        self.__lbl_photo = tk.Label(self.frame, image=self.python_image)
        self.__lbl_photo.grid(row=2, column=0)
