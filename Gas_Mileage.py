 # Write a GUI program that calculates a car's gas mileage.
 # The program's window should have Entry widgets that let the user enter the number of gallons of gas the car holds,
 # and the number of miles it can be driven on a full tank.  When a Calculate MPG button is clicked,
 # the program should display the number of miles that the car may be driven per gallon of gas.
 # Use the following formula to calculate miles per gallon:  MPG = miles / gallons.


import tkinter
from tkinter import messagebox

class Gas_Mileage_GUI:
    def __init__(self):

            ## Create window
        self.main_window = tkinter.Tk()

            ## Create Window Title
        self.main_window.title("Gas Mileage Calculator")