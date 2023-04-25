FROM python:3.8-bullseye as base
WORKDIR /app
COPY . .
RUN sh ./setup.sh
EXPOSE 80

FROM base
ENV FLASK_APP=server.py
ENV FLASK_RUN_PORT=80
CMD "flask run"
