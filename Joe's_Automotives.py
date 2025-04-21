    # Joe's Automotive performs the following routine maintenance service:

    # Oil Change - $30.00
    # Lube Job - $20.00
    # Radiator Flush - $40.00
    # Transmission Fluid - $100.00
    # Inspection - $35.00
    # Muffler replacement - $200.00
    # Tire Rotation - $20.00

    # Write a GUI with check buttons that allows the user to select any or all of these services.
   # When the user clicks a button, the total charges should be displayed.

import tkinter
from tkinter import messagebox


class Joes_Automotives_GUI:
    def __init__(self):

            ## Create window
        self.main_window = tkinter.Tk()

            ## Create Window Title
        self.main_window.title("Joe's Automotive")