"""
Simple HTTP server to serve the QR code detector web app.
Run this and access from your phone on the same network.
"""

import http.server
import socket
import os
import sys

PORT = 8080  # Changed to more common port

def get_local_ip():
    """Get the local IP address of this machine."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    local_ip = get_local_ip()
    
    print("=" * 60)
    print("  QR CODE DETECTOR - Web Server")
    print("=" * 60)
    print()
    print(f"Server starting on port {PORT}...")
    print()
    print("=" * 60)
    print("  ACCESS URLS:")
    print("=" * 60)
    print()
    print(f"  On this Mac:     http://localhost:{PORT}")
    print(f"  On your phone:   http://{local_ip}:{PORT}")
    print()
    print("=" * 60)
    print("  INSTRUCTIONS FOR ANDROID:")
    print("=" * 60)
    print()
    print("  1. Make sure your phone is on the SAME WiFi network")
    print(f"  2. Open Chrome and go to: http://{local_ip}:{PORT}")
    print()
    print("  If camera doesn't work, enable this Chrome flag:")
    print("    chrome://flags/#unsafely-treat-insecure-origin-as-secure")
    print(f"    Add: http://{local_ip}:{PORT}")
    print()
    print("=" * 60)
    print("  Press Ctrl+C to stop")
    print("=" * 60)
    print()
    
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
            print(f"Server running! Waiting for connections...")
            print()
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"ERROR: Port {PORT} is already in use!")
            print(f"Try running: lsof -i :{PORT}")
            print("Or wait a moment and try again.")
        else:
            print(f"ERROR: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nServer stopped. Goodbye!")

if __name__ == "__main__":
    main()
