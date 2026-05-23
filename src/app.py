from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Flask Application"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP"
    })

@app.route('/users')
def users():
    return jsonify([
        {"id": 1, "name": "Venkatesh"},
        {"id": 2, "name": "Rahul"},
        {"id": 3, "name": "Anil"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)