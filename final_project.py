from tkinter import *

# Set up the main window
screen = Tk()
screen.minsize(width=400, height=150)
screen.title("Mile to Km Converter")
screen.configure(bg="#2E2E2E", padx=30, pady=20)  # Dark background for modern look

# Entry box for Miles input
entry = Entry(width=10, font=("Arial", 14), bg="#F0F0F0", fg="#333", borderwidth=2)
entry.grid(column=1, row=0, padx=(0, 10), pady=(0, 10))

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 12), bg="#2E2E2E", fg="#FFFFFF")
miles_label.grid(column=2, row=0, padx=(0, 10), pady=(0, 10))

# "Is equal to" label
is_equal_to_label = Label(text="Is equal to", font=("Arial", 12), bg="#2E2E2E", fg="#FFFFFF")
is_equal_to_label.grid(column=0, row=1, padx=(0, 10), pady=(10, 10))

# Result label for displaying converted km
miles_to_km = Label(text="0", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="#4CAF50")
miles_to_km.grid(column=1, row=1, pady=(10, 10))

# Km Label
km_label = Label(text="Km", font=("Arial", 12), bg="#2E2E2E", fg="#FFFFFF")
km_label.grid(column=2, row=1, padx=(10, 0), pady=(10, 10))

# Calculate Button
def calculate():
    try:
        miles = float(entry.get())
        km = miles * 1.60934
        miles_to_km.config(text=f"{km:.2f}")  # Limit to 2 decimal places
    except ValueError:
        miles_to_km.config(text="Error")

calculate_button = Button(
    text="Calculate",
    command=calculate,
    font=("Arial", 12, "bold"),
    bg="#4CAF50", fg="white",
    activebackground="#66BB6A", activeforeground="white",
    borderwidth=0,
    padx=10, pady=5
)
calculate_button.grid(column=1, row=2, pady=(10, 0))

# Configure grid columns for alignment
screen.grid_columnconfigure(0, weight=1)
screen.grid_columnconfigure(3, weight=1)

screen.mainloop()
