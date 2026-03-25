from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hi!</h1><p>Welcome to your Dockerized Python app.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
