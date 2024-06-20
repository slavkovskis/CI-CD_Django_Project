FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000 & sleep infinity"]
