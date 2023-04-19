import requests as requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

from user import User

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    user1 = User("Klm", 22)
    user2 = User("Sbr", 21)
    import http.client
    api_domain = "countriesnow.space"
    conn = http.client.HTTPSConnection(api_domain)
    headersList = {
        "Accept": "*/*",
    }
    payload = ""
    conn.request("GET", "/api/v0.1/countries", payload, headersList)
    response = conn.getresponse()
    result = response.read()
    return result


@app.route("/scrap", methods=['GET'])
def get_web_info():
    import http.client
    api_domain = "flipkart.com"
    conn = http.client.HTTPSConnection(api_domain)
    headersList = {
        "Accept": "*/*",
    }
    payload = ""
    conn.request("GET", "", payload, headersList)
    response = conn.getresponse()
    result = response.read()
    return str(result)


@app.route('/scrap-of', methods=['GET'])
def scrapper():
    url = request.args.get("url")
    try:
        webpage = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(webpage.content, "html.parser")
        list_data = str(soup).replace("\n", "").split(" ")
        return jsonify({"data": list_data})
    except Exception as error:
        return "Error Scrapping " + str(error.args)


@app.route("/", methods=["POST", 'GET'])
def post_api():
    return jsonify({})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
