import json
import os
import time
from urllib.parse import unquote

import pandas as pd
from flask import Flask, send_file, request, jsonify, Response
from flask_sockets import Sockets

from log import logger, error_handler
from setting import XLSX_PATH
from work import run

app = Flask(__name__)
sockets = Sockets(app)


@app.route('/')
def index():
    return send_file('templates/index.html')


@app.route('/work')
def work():
    return send_file('templates/work.html')


@sockets.route('/echo')
def echo(ws):
    q = request.args.get('q')
    data = json.loads(unquote(q))
    try:
        run(data, ws)
        ws.send(json.dumps({'success': True}))
    except Exception as e:
        ws.send(json.dumps({'error': str(e)}))
        error_handler(e)
    return


@app.route('/xlsx', methods=['POST'])
def create_xlsx():
    info_list = request.json.get('info_list')
    df = pd.DataFrame(info_list)
    xlsx_name = '{}.xlsx'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
    df.to_excel(os.path.join(XLSX_PATH, xlsx_name))
    return jsonify(xlsx_name=xlsx_name)


@app.route('/xlsx/<xlsx_name>')
def get_xlsx(xlsx_name):
    try:
        return send_file(os.path.join(XLSX_PATH, xlsx_name))
    except Exception as e:
        error_handler(e)
        return Response('文件不存在', 404)


@app.route('/ping')
def ping():
    return jsonify(msg='pong')
