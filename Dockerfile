FROM python:3.8-bullseye as base
WORKDIR /app
COPY . .
RUN bash setup.sh

EXPOSE 5000
CMD [" python" ,"server.py" ]
