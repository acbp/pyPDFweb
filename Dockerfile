FROM python:3.8-bullseye 
WORKDIR /app
COPY . .
RUN sh ./setup.sh
EXPOSE 80
RUN FLASK_APP=server.py
RUN FLASK_RUN_PORT=80
CMD "flask run"
