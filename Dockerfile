FROM python:3.8-bullseye

COPY . .
RUN bash setup.sh

EXPOSE 5000

CMD ["python","test.py"]
