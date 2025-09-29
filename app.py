# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Docker + PyCharm!"


@app.route("/api/index", methods = ["GET"])
def Index():
    return jsonify({"message":"Hello REST API GET"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

