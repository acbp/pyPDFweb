FROM python:3.8-bullseye 
WORKDIR /app
COPY . .
RUN sh ./setup.sh
CMD "flash run"
