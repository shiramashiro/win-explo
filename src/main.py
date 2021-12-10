from flask import Flask, request
from flask_cors import cross_origin
import os
import shift
import dissect
import psutil
import json

app = Flask(__name__)


@app.route('/getwin/drives', methods=['POST'])
@cross_origin()
def getwin_dirves():
    """
    获取Windows系统所有系统盘符
    :return:
    """
    """
    获取Windows操作系统上的所有盘符
    :return: 返回当前Windows系统上的所有盘符
    """
    drives = []
    for drive in psutil.disk_partitions():
        drives.append(drive[0])
    return {
        'drives': drives
    }


@app.route('/getwin/dircs', methods=['POST'])
@cross_origin()
def getwin_dirs():
    data = json.loads(request.data.decode('utf-8'))
    childircpath = ''
    for item in data['dircs']:
        childircpath += item + '\\'
    dircpath = os.path.join(data['drive'], childircpath)
    dircs = []
    for dirc in dissect.listdirs(dircpath):
        last = os.path.split(dirc)[1]
        dircs.append({
            'value': last,
            'label': last
        })
    return {
        'dircs': dircs
    }


@app.route('/extractname', methods=['POST'])
@cross_origin()
def extractname():
    src = request.form.get('src')
    dst = request.form.get('dst')
    pat = request.form.get('pat')
    shift.extractname(src, dst, pat)
    return 'ok'


if __name__ == '__main__':
    app.run()
