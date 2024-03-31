from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

def read_csv(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        return data
    except Exception as e:
        print("Error reading CSV file:", e)
        return None

@app.route('/')
def display_csv():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(current_dir, '..', '..', '..', 'main', 'log', 'log.csv')
    data = read_csv(csv_filename)
    if data is not None:
        print(data)
        return render_template('index.html', data=data)
    else:
        return "An error occurred while reading the CSV file."

if __name__ == '__main__':
    app.run(debug=True)
