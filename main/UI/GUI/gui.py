import tkinter as tk
from tkinter import ttk
import pandas as pd
import threading
import time
import os

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
        
        self.refresh_thread = threading.Thread(target=self.update_periodically)
        self.refresh_thread.daemon = True 
        self.refresh_thread.start()
        
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
    
    def update_dataframe(self, df):
        self.table.delete(*self.table.get_children())
        for index, row in df.iterrows():
            self.table.insert("", "end", values=[row[col] for col in self.columns])
            
    def update_periodically(self):
        while True:
            self.update_table()
            time.sleep(1) 

def main():
    root = tk.Tk()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(current_dir, '..', '..', 'log', 'log.csv')
    app = LogViewerApp(root, log_file)
    root.mainloop()

if __name__ == "__main__":
    main()
