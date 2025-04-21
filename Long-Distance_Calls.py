    # A long-distance provider charges the following rates for telephone calls:

    # Rate Category	Rate per Minute
    # Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
    # Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
    # Off-Peak (midnight through 5:59 P.M.) 	$0.05

    # Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
    # and enter the number of minutes of the call into an Entry widget.
    # An info dialog box  should display the charge for the call.

import tkinter
from tkinter import messagebox


class Long_Distance_Calls_GUI:
    def __init__(self):

            ## Create window
        self.main_window = tkinter.Tk()

            ## Create Window Title
        self.main_window.title("Long-Distance Calls Calculator")
