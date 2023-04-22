FROM python:3.11-bullseye

COPY . .
RUN bash setup.sh

EXPOSE 5000

CMD ["python","test.py"]
