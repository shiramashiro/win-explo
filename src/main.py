import os
import json
import shift
from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/extractname', methods=['POST'])
@cross_origin()
def extractname():
    code = 200
    data = json.loads(request.data.decode('utf-8'))
    if os.path.exists(data['src']) and os.path.exists(data['dst']):
        shift.extractname(data['src'], data['dst'], data['pat'])
    else:
        code = 500
    return {
        'code': code
    }


if __name__ == '__main__':
    app.run()
