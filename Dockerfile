FROM python:3.8-bullseye 
WORKDIR /app
COPY . .
RUN sh ./setup.sh
EXPOSE 80
CMD "flask run"
