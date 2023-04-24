FROM python:3.8-bullseye as base
WORKDIR /app
COPY . .
RUN bash setup.sh

EXPOSE 5000
#CMD [ "python" ,"server.py" ]
CMD [ "gunicorn","-b 0.0.0.0", "-p 5000", "'server:app'"]
