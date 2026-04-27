from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if data is None or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing fields: a, b'}), 400
    return jsonify({'result': data['a'] + data['b']})


@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if data is None or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing fields: a, b'}), 400
    return jsonify({'result': data['a'] - data['b']})


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if data is None or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing fields: a, b'}), 400
    return jsonify({'result': data['a'] * data['b']})


@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data is None or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Missing fields: a, b'}), 400
    if data['b'] == 0:
        return jsonify({'error': 'Division by zero'}), 400
    return jsonify({'result': data['a'] / data['b']})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
