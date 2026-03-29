from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.remote_addr
    with open("ip_log.txt", "a") as f:
        f.write(f"{ip} - {socket.gethostname()}\n")
    return "Your IP address has been logged!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)