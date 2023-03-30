from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/member", methods=["GET", "POST"])
def get_api():
    # print(request.json)
    print(request.args.get("p"))
    if request.method == 'POST':
        return jsonify({
            "message": "POST method is not allowed"
        })
    return jsonify(request.args)


@app.route("/add", methods=["POST"])
def post_api():
    print(request.json)
    print(request.args.get())
    if request.method == 'GET':
        return jsonify({
            "message": "GET method is not allowed"
        })
    return jsonify(request.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
