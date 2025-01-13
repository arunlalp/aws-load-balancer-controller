from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    custom_header = request.headers.get('X-Custom-Header')
    return jsonify({
        "message": f"Hello from Flask! Custom header received: {custom_header}"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)