FROM python:3.5
ENV APP /app
RUN mkdir $APP
WORKDIR $APP
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
