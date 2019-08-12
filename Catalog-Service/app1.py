from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def hello():   
    html = "<h3>Hello APP1 {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
	   "<b>Hello World! I have been seen</b> {count}<br/> <b>times.\n</b>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), count = redis.incr('hits'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
