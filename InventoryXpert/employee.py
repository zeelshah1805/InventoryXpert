from tkinter import *
from PIL import Image, ImageTk
import time

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("InventoryXpert | Developed by Zeel Shah")
        self.root.config(bg="#f2f2f2")
        
if __name__ == "__main__":
    root = Tk()
    app = employeeClass(root)
    root.mainloop()