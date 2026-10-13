#!/usr/bin/env python3
"""
High-performance Threading HTTP Server for Agrolink Africa Website.
Serves from /home/pirate101/Downloads/agri
Redirects '/' to '/agribusiness.cmsmasters.studio/main/index.html'
Ensures proper MIME types for web fonts, SVG, and WebP images.
"""

import http.server
import os
import sys

PORT = 8080
DIRECTORY = '/home/pirate101/Downloads/agri'

class AgrolinkHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        clean_path = self.path.split('?')[0].split('#')[0]
        if clean_path in ('', '/', '/index.html'):
            self.send_response(302)
            self.send_header('Location', '/agribusiness.cmsmasters.studio/main/index.html')
            self.end_headers()
            return
        return super().do_GET()

    def guess_type(self, path):
        ctype = super().guess_type(path)
        if path.endswith('.webp'):
            return 'image/webp'
        elif path.endswith('.svg'):
            return 'image/svg+xml'
        elif path.endswith('.woff2'):
            return 'font/woff2'
        elif path.endswith('.woff'):
            return 'font/woff'
        elif path.endswith('.ttf'):
            return 'font/ttf'
        return ctype

def run_server():
    os.chdir(DIRECTORY)
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.ThreadingHTTPServer(server_address, AgrolinkHTTPRequestHandler)
    print(f"Agrolink Africa local server running at:")
    print(f"  -> http://localhost:{PORT}/")
    print(f"  -> http://127.0.0.1:{PORT}/")
    print(f"Serving from: {DIRECTORY}")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")

if __name__ == '__main__':
    run_server()
