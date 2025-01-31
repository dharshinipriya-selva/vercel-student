import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS for all origins
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Parse the query parameters
        query = urlparse(self.path).query
        params = parse_qs(query)
        names = params.get('name', [])

        # Load the marks data from the JSON file
        try:
            with open('gewrcel-python.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.wfile.write(json.dumps({"error": "Marks data not found"}).encode())
            return

        # Extract marks for the requested names
        result = {"marks": {}}
        for name in names:
            mark = data.get(name)
            if mark is not None:
                result["marks"][name] = mark

        # Respond with the marks as JSON
        self.wfile.write(json.dumps(result).encode())

# This part is needed for local testing but is ignored by Vercel
if __name__ == '__main__':
    PORT = 3000 
    httpd = HTTPServer(('', PORT), handler)
    print(f"Serving at port {PORT}")
    httpd.serve_forever()