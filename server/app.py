from flask import Flask



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return ("Checking the docs to see how to run the basic wrong application ")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')