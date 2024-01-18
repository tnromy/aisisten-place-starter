from flask import Flask, request

app = Flask(__name__)

@app.route('/sentiment/place', methods=['GET'])
def index():
    return "halo guys"

@app.route('/sentiment/place/api/find-place', methods=['POST'])
def findPlace():
    return "masuk"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
