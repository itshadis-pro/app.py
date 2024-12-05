import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize the main window
window = tk.Tk()
window.title("Countdown Timer")
window.geometry("400x250")  # Adjusted size for additional input fields

# Time display label
time_label = tk.Label(window, text="", font=("Helvetica", 16), justify="center")
time_label.pack(pady=20)  # Add some padding

# Entry field for the user to input the target date
date_label = tk.Label(window, text="Enter the date you wish to count down (YYYY-MM-DD):", font=("Helvetica", 12))
date_label.pack()
date_entry = tk.Entry(window, font=("Helvetica", 14))
date_entry.pack(pady=10)

# Function to calculate and display the countdown
def countdown(target_date):
    # Current date and time
    now = datetime.now()

    # Calculate the time difference
    remaining_time = target_date - now

    if remaining_time.total_seconds() <= 0:
        time_label.config(text="Time's up!")
        return

    # Break down the time difference
    days = remaining_time.days
    seconds_left = remaining_time.total_seconds()
    hours, remainder = divmod(seconds_left, 3600)
    minutes, seconds = divmod(remainder, 60)
    months = days // 30  # Approximation for months

    # Format the time display
    count_text = (
        f"Months: {months}\n"
        f"Days: {days}\n"
        f"Hours: {int(hours) % 24}\n"
        f"Minutes: {int(minutes)}\n"
        f"Seconds: {int(seconds)}"
    )

    # Update the label
    time_label.config(text=count_text)

    # Schedule the function to run again after 1 second
    window.after(1000, countdown, target_date)

# Function to start the countdown
def start_timer():
    try:
        # Parse the user input date
        user_date = date_entry.get()
        target_date = datetime.strptime(user_date, "%Y-%m-%d")

        # Start the countdown
        countdown(target_date)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in the format YYYY-MM-DD.")

# Start button
start_button = tk.Button(window, text="Start Countdown", command=start_timer, font=("Helvetica", 14))
start_button.pack(pady=20)

# Run the main event loop
window.mainloop()
