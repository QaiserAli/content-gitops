from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello and Welcome to GitOps world. This change is done in feature branch!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
