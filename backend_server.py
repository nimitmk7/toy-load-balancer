from flask import Flask, Response, jsonify
import requests
import sys

app = Flask(__name__)

# Default values
server_number = 1
port = 5001

@app.route("/hello", methods=["GET"])
def handle_request():
    return f"Hello from Backend Server #{server_number} on port {port}!"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python request_server.py <port> <strategy>")
        sys.exit(1)
    
    port = int(sys.argv[1])
    server_number = int(sys.argv[2])

    app.run(port=port, debug=True)

