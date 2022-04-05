from flask import Flask, request
from task_five import search
import json

app = Flask(__name__)


@app.route('/search')
def search_something():
    if 'query' in request.args.keys():
        result = search(request.args['query'])
        return json.dumps(result)
    else:
        return json.dumps({'errors': 'You must enter query parameter'})


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=8080)
