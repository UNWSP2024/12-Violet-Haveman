 # Write a GUI program that calculates a car's gas mileage.
 # The program's window should have Entry widgets that let the user enter the number of gallons of gas the car holds,
 # and the number of miles it can be driven on a full tank.  When a Calculate MPG button is clicked,
 # the program should display the number of miles that the car may be driven per gallon of gas.
 # Use the following formula to calculate miles per gallon:  MPG = miles / gallons.




import tkinter as tk
from tkinter import messagebox

class GasMileageGUI:
    def __init__(self):
        # Main window
        self.main_window = tk.Tk()
        self.main_window.title("Gas Mileage Calculator")

        # Top frame for input
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Gallons input
        self.gallon_label = tk.Label(self.top_frame, text="Enter gallons:")
        self.gallon_entry = tk.Entry(self.top_frame)

        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')

        # Miles input
        self.miles_label = tk.Label(self.mid_frame, text="Enter miles:")
        self.miles_entry = tk.Entry(self.mid_frame)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Result label
        self.result = tk.StringVar()
        self.result_label = tk.Label(self.bottom_frame, textvariable=self.result)

        # Buttons
        self.calc_button = tk.Button(self.bottom_frame, text="Calculate MPG", command=self.show_info)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        self.result_label.pack()
        self.calc_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)

        # Pack frames
        self.top_frame.pack(pady=5)
        self.mid_frame.pack(pady=5)
        self.bottom_frame.pack(pady=10)

        # Start the GUI loop
        tk.mainloop()

    def show_info(self):
        try:
            gallons = float(self.gallon_entry.get())
            miles = float(self.miles_entry.get())
            if gallons <= 0:
                raise ValueError("Gallons must be greater than 0")
            mpg = miles / gallons
            self.result.set(f"Miles per gallon: {mpg:.2f}")
        except ValueError as e:
            messagebox.showerror("Input error", f"Invalid input: {e}")

# Run the program
if __name__ == '__main__':
    GasMileageGUI()



