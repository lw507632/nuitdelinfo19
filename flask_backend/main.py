from flask import Flask, json, Response, request
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)

your_rest_server_port = 5000
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://eureka-server:8761",
                   app_name="python_flask_app",
                   instance_port=your_rest_server_port)

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
        res = {'body':[]}
        for k in aides_mock.keys():
            for key, item in aides_mock[k].items():
                for key2, item2 in req_data.items():
                    if item==item2:
                        tmp.add(k)
        res['body'].extend(list(tmp))
        res['status'] = 200
        return res

if __name__ == '__main__':
    app.run()
