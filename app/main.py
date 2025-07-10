from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv('PORT', 8000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"RPI Core Service is running!\n")

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"Starting server at http://0.0.0.0:{PORT}")
    server.serve_forever()
