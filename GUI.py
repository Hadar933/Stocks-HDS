import tkinter as tk

SEG_SIZE = 80  # the dimensions will be based on this constant segment size
COL = 7
ROW = 6
SIZE = '720x560'

class GUI:

    def __init__(self):
        """
        a constructor for GUI object
        """
        self.width = (COL + 2) * SEG_SIZE
        self.height = (ROW + 1) * SEG_SIZE
        self.font = 'Times'
        self.root = tk.Tk()  # root for the main menu
        self.canvas = None

    def set_canvas(self, new_canvas):
        self.canvas = new_canvas

    def start_screen(self):
        self.root.geometry(SIZE)
        self.root.mainloop()


gui=GUI()
gui.start_screen()

