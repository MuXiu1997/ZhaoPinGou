import multiprocessing

from gevent import monkey

monkey.patch_all()


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


if __name__ == '__main__':
    from app import app
    from scheduler import scheduler
    from server import StandaloneApplication

    scheduler().start()

    options = {
        'bind': '{host}:{port}'.format(host='0.0.0.0', port=5000),
        'workers': number_of_workers(),
        'worker_class': 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker',
        'worker_tmp_dir': '/dev/shm',
    }
    server = StandaloneApplication(app, options)
    server.run()

    # from app import app
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    #
    # server = pywsgi.WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    # print('server start')
    # server.serve_forever()
