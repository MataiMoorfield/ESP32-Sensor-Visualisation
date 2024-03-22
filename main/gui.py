import tkinter as tk
from tkinter import ttk
import pandas as pd
import threading
import time

class LogViewerApp:
    def __init__(self, root, log_file):
        self.root = root
        self.log_file = log_file
        self.root.title("Log Viewer")
        
        self.table = ttk.Treeview(self.root)
        
        self.columns = self.get_csv_columns()
        
        self.table['columns'] = self.columns
        
        for col in self.columns:
            self.table.column(col, anchor=tk.W, width=150)
            self.table.heading(col, text=col, anchor=tk.W)
        
        self.table.pack(expand=True, fill=tk.BOTH)
        
        self.update_table()
        
    def get_csv_columns(self):
        try:

            df = pd.read_csv(self.log_file, nrows=1)
            return df.columns.tolist()
        except Exception as e:
            print("Error:", e)
            return []
        
    def update_table(self):
        try:
            df = pd.read_csv(self.log_file)
            self.update_dataframe(df)
        except Exception as e:
            print("Error:", e)
            
        self.root.after(1000, self.update_table)
        
    def update_dataframe(self, df):
        self.table.delete(*self.table.get_children())
        for index, row in df.iterrows():
            self.table.insert("", "end", values=[row[col] for col in self.columns])

def main():
    root = tk.Tk()
    app = LogViewerApp(root, "log/log.csv")
    root.mainloop()

if __name__ == "__main__":
    main()
