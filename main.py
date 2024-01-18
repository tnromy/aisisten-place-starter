from flask import Flask, request

app = Flask(__name__)

@app.route('/place', methods=['GET'])
def index():
    return "halo guys"

@app.route('/place/api/find-place', methods=['POST'])
def findPlace():
    return "masuk"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
