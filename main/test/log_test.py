# Run to test the logger

import http.server
import json
from io import BytesIO

class JSONHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = [
            {"Temperature": 24, "Humidity": 90, "Light": 57},
            {"Temperature": 23, "Humidity": 89, "Light": 58},
            {"Temperature": 24, "Humidity": 91, "Light": 58}
        ]
        
        self.wfile.write(json.dumps(data).encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, JSONHandler)
    print('Starting server on port', port)
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
