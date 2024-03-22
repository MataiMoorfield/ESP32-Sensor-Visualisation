import requests
import csv
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_store_data(url, csv_filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data:  
            with open(csv_filename, 'w', newline='') as csvfile:
                fieldnames = data.keys() 
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerow(data)
                
            logging.info("Data stored successfully in %s", csv_filename)
        else:
            logging.warning("No data received from the server")
    else:
        logging.error("Failed to fetch data from the provided URL")

def update_csv_periodically(url, csv_filename, interval_seconds=1):
    logging.info("Starting CSV update process...")
    while True:
        fetch_and_store_data(url, csv_filename)
        logging.info("CSV file updated. Waiting for %d seconds before the next update...", interval_seconds)
        time.sleep(interval_seconds)

if __name__ == '__main__':
    url = 'http://192.168.1.39'
    csv_filename = 'log.csv'
    update_csv_periodically(url, csv_filename)
