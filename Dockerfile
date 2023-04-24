FROM python:3.8-bullseye 
WORKDIR /app
COPY . .
RUN sh ./setup.sh

EXPOSE 5000
#CMD [ "python" ,"server.py" ]
CMD [ "gunicorn","-b 0.0.0.0", "-p 5000", "'server:app'"]
