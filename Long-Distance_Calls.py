    # A long-distance provider charges the following rates for telephone calls:

    # Rate Category	Rate per Minute
    # Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
    # Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
    # Off-Peak (midnight through 5:59 P.M.) 	$0.05

    # Write a GUI application that allows the user to select a rate category (from a set of radio buttons),
    # and enter the number of minutes of the call into an Entry widget.
    # An info dialog box  should display the charge for the call.

import tkinter as tk
from tkinter import messagebox

class LongDistanceGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Long Distance Call Charge Calculator")

        # Create the shared variable for radio buttons
        self.rate_var = tk.StringVar()
        self.rate_var.set("Daytime")  # Default selection

        # Rate options and labels
        self.rates = {
            'Daytime': 0.02,
            'Evening': 0.12,
            'Off-Peak': 0.05
        }

        # Create radio buttons for rate selection
        tk.Label(self.main_window, text="Select Rate Category:").pack(anchor='w')
        for rate in self.rates:
            tk.Radiobutton(
                self.main_window,
                text=f"{rate} (${self.rates[rate]:.2f}/min)",
                variable=self.rate_var,
                value=rate
            ).pack(anchor='w', padx=10)

        # Entry for minutes
        tk.Label(self.main_window, text="Enter number of minutes:").pack(anchor='w', pady=(10, 0))
        self.minutes_entry = tk.Entry(self.main_window)
        self.minutes_entry.pack(padx=10, pady=(0, 10))

        # Calculate button
        self.calc_button = tk.Button(self.main_window, text="Calculate Charge", command=self.calculate_charge)
        self.calc_button.pack(pady=5)

        # Start the main loop
        tk.mainloop()

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                raise ValueError("Minutes cannot be negative.")
            rate_category = self.rate_var.get()
            charge = minutes * self.rates[rate_category]
            messagebox.showinfo("Call Charge", f"Rate: {rate_category}\nMinutes: {minutes}\nCharge: ${charge:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes.")

if __name__ == '__main__':
    LongDistanceGUI()
