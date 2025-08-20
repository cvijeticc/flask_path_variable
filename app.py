from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return {"message": "Hello, world!"}, 200

@app.route('/hello/<name>', methods=['GET'])
def hello_with_name(name):
    return {"message": f"Hello, {name}!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
