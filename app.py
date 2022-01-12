import os
from flask import Flask
if os.path.exists("env.py"):
    import env 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hellow World.... again!"


if __name__ == "__name__":
    app.run(host=os.environ.get("IP"),
            port=int(host.os.environ.get("PORT")),
            debug=True)