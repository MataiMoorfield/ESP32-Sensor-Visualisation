import csv
import tkinter as tk

def read_csv(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def update_data():
    # Clear the text widget before updating
    text_widget.delete(1.0, tk.END)
    
    # Read the CSV file again to update the data
    data = read_csv(csv_filename)
    
    # Insert CSV data into the text widget
    for row in data:
        text_widget.insert(tk.END, str(row) + "\n")
    
    # Schedule the next update after 1 second
    text_widget.after(1000, update_data)

# Create a Tkinter window
window = tk.Tk()
window.title("CSV Data")

# Create a text widget to display CSV data
text_widget = tk.Text(window)
text_widget.pack()

# Read the CSV data initially
csv_filename = 'log/log.csv'
update_data()

# Start the Tkinter event loop
window.mainloop()
