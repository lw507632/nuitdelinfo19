from flask import Flask, json, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/oui_non", methods=["GET", "POST"])
def oui_non():
    data = {
        'hello': 'world',
        'number': 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
