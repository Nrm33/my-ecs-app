from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Hello, This is Nikhil! My Flask app is running inside Docker."

@app.route('/info')
def info():
    return jsonify({
        "app_name": "Demo Flask App",
        "status": "Running Successfully",
        "developer": "Nikhil Ramesh Mali"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
