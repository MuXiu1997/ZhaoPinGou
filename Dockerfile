FROM python:3.7.5

COPY . /app/

WORKDIR /app

RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt

EXPOSE 5000

CMD python server.py