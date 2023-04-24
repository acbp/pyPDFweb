FROM python:3.8-bullseye 
WORKDIR /app
COPY . .
RUN sh ./setup.sh

#CMD [ "python" ,"server.py" ]
CMD [ "gunicorn","-b 0.0.0.0", "server:app"]
