FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

ADD ./ /app/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN adduser -u 1234 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

EXPOSE 8080

CMD ["python", "drf_jwt_backend/manage.py", "runserver", "0.0.0.0:8000"]