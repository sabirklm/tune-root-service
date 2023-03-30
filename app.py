from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{}])


@app.route("/", methods=["POST", 'GET'])
def post_api():
    return jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
