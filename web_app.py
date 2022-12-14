from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world! 202211042304</p>"

@app.route("/test")
def exec_test():
    return "<p>TestTest!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
