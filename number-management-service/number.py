from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    merged_numbers = set()

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            numbers = set(response.json().get('numbers', []))
            merged_numbers.update(numbers)

    response_data = {
        "numbers": list(merged_numbers)
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
