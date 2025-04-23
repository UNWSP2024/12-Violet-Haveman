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

            # Create a listbox widget
        self.car_listbox = tkinter.Listbox(
            self.main_window, width = 0, height = 0)
        self.car_listbox.pack(padx= 0, pady=5)

            # Create a list of services
        self.services = {
            'Oil Change': 30.0,
            'Lube Job': 20.0,
            'Radiator Flush': 40.0,
            'Transmission Fluid': 35.0,
            'Inspection':35.0,
            'Muffler Replacement':200.0,
            'Tire Rotation':20.0
        }
        # Store IntVar for each checkbox
        self.service_vars = {}

        # Create checkbuttons
        for service, price in self.services.items():
            var = tkinter.IntVar()
            cb = tkinter.Checkbutton(
                self.main_window,
                text=f"{service} - ${price:.2f}",
                variable=var
            )
            cb.pack(anchor='w', padx=10, pady=2)
            self.service_vars[service] = var

        # Button to calculate total
        self.total_button = tkinter.Button(
            self.main_window,
            text="Calculate Total",
            command=self.calculate_total
        )
        self.total_button.pack(pady=10)

        tkinter.mainloop()

    def calculate_total(self):
        total = 0.0
        selected_services = []
        for service, var in self.service_vars.items():
            if var.get() == 1:
                total += self.services[service]
                selected_services.append(service)

        if selected_services:
            messagebox.showinfo(
                "Total Charges",
                f"Selected Services:\n" +
                "\n".join(selected_services) +
                f"\n\nTotal: ${total:.2f}"
            )
        else:
            messagebox.showinfo("Total Charges", "No services selected.")

if __name__ == '__main__':
    Joes_Automotives_GUI()