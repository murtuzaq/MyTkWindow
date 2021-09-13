import tkinter as tk
from tkinter import LEFT


class ColorButton:
    def __init__(self, frame, color, callback):
        self.__button = tk.Button(frame, text=color.capitalize(), command=lambda: callback(color), background = color)
        self.__button.pack(side=LEFT)
