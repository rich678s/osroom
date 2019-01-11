FROM python:3.5
ENV APP /app
RUN mkdir $APP
WORKDIR $APP
COPY . .
RUN setmirror.sh
RUN pip install -r requirements.txt
CMD python start.py
