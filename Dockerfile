FROM python:3.5
ENV APP /app
RUN mkdir $APP
WORKDIR $APP
COPY requirements.txt .
RUN pip install -i  http://mirrors.aliyun.com/pypi/simple/  --trusted-host=mirrors.aliyun.com  -r requirements.txt
CMD python start.py
