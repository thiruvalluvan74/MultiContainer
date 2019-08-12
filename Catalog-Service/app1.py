from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def hello():   
    html = "<h3>Hello APP1{name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" 
    return html.format(name=os.getenv("NAME", "APP1 - world"), hostname=socket.gethostname())
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
