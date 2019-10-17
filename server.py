import multiprocessing
import time

from flask import Flask, request, jsonify, render_template, send_file, Response

from work import run

app = Flask(__name__, static_url_path='', static_folder='./templates')

queue = multiprocessing.Queue()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/work', methods=['POST'])
def work():
    data = request.json
    work_name = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    data['work'] = work_name
    queue.put(data)
    return jsonify(errCode=0, work=work_name)


@app.route('/xlsx/<work_name>')
def xlsx(work_name):
    file_name = '{}.xlsx'.format(work_name)
    try:
        return send_file('./xlsx/{}'.format(file_name))
    except FileNotFoundError:
        return Response("""
<html>
<head>
  <script>
    let i = 4;
    let timer;
    timer = setInterval("fun()", 1000);

    function fun() {
      if (i === 0) {
        location.reload();
        clearInterval(timer);
        return
      }
      document.getElementById("mes").innerHTML = `${i}`;
      i--;
    }
  </script>
  <title></title>
</head>
<body>
<div id="errorfrm">
  <div>
    <p>任务执行中，请稍候， <span id="mes">5</span> 秒钟后将刷新网页重试</p>
  </div>

</div>
</body>
</html>""")


def word(q):
    while True:
        data = q.get(True)
        run(data)


if __name__ == '__main__':
    pw = multiprocessing.Process(target=word, args=(queue,))
    pw.start()
    app.run()
