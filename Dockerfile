FROM python:3.7.4

COPY . /app/

COPY /etc/localtime /etc/localtime

WORKDIR /app

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 5000

CMD python server.py