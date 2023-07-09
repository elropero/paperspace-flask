FROM paperspace/flask-app-base:2023-06-16

WORKDIR /app

COPY app ./app
COPY requirements.txt ./

RUN pip3 install -U pip && pip3 install -r requirements.txt

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.main:app", "--loglevel", "debug"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--worker-tmp-dir", "/dev/shm", "--workers", "2", "--threads", "4", "--worker-class", "gthread", "app.main:app"]
 