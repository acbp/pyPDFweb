FROM python:3.8-bullseye as base
COPY . .
RUN bash ./setup.sh

FROM base
ENV FLASK_APP=server.py
ENV FLASK_RUN_PORT=80
EXPOSE 80

ENTRYPOINT ["python", "-m"]
CMD [ "flask", "run" ]
