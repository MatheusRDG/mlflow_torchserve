from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


@app.route("/api", methods=["POST"])
def api():
    data = request.json
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)
