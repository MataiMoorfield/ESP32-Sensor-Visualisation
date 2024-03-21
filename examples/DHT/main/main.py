from flask import Flask, render_template
import csv

app = Flask(__name__)

def read_csv(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

@app.route('/')
def display_csv():
    csv_filename = 'log/log.csv'
    data = read_csv(csv_filename)
    print(data) 
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
