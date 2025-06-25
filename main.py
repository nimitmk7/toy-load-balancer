from flask import Flask, Response, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

STRATEGY = os.getenv("STRATEGY")
NO_OF_SERVERS = os.getenv("NO_OF_SERVERS")
SERVER_PORTS = os.getenv("BACKEND_SERVER_PORTS", "").split(",")

# Construct backend URLs
last_served_server_id = 1

@app.route("/info", methods=["GET"])
def get_load_balancer_info():
    if not STRATEGY:
        return Response("Strategy not set", status=400)
    if not NO_OF_SERVERS:
        return Response("No of servers not set", status=400)

    info_dict = {
        "strategy": STRATEGY,
        "no_of_servers": NO_OF_SERVERS,
        "servers": []
    }
    return jsonify(info_dict)

@app.route("/hello", methods=["GET"])
def route_request():
    if not STRATEGY:
        return Response("Strategy not set", status=400)
    if not NO_OF_SERVERS:
        return Response("No of servers not set", status=400)

    global last_served_server_id
    last_served_server_id = (last_served_server_id + 1) % int(NO_OF_SERVERS)
    print(SERVER_PORTS)
    backend_server_port = SERVER_PORTS[last_served_server_id-1]
    response = requests.get(f"http://localhost:{backend_server_port}/hello")
    return response.text


if __name__ == "__main__":
    app.run(port=8000, debug=True)



