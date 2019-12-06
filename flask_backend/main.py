from flask import Flask, json, Response, request

app = Flask(__name__)
with open('aides_mock.json') as f:
    aides_mock = json.load(f)


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

@app.route("/aides", methods=["POST"])
def aides():
    

    if request.method == "POST":
        req_data = request.get_json()
        tmp = set()
        res = {'aides':[]}
        for k in aides_mock.keys():
            for key, item in aides_mock[k].items():
                for key2, item2 in req_data.items():
                    if item==item2:
                        tmp.add(k)
        res['aides'].extend(list(tmp))
        return res

if __name__ == '__main__':
    app.run()
