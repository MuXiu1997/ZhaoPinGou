FROM python:3.7.5

COPY requirements.txt /

RUN pip install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt && \
rm -f requirements.txt && \
mkdir /app

WORKDIR /app

COPY . /app

RUN chmod +x entrypoint.sh && \
ln -s /app/entrypoint.sh /usr/local/bin/

ENTRYPOINT entrypoint.sh

EXPOSE 5000

