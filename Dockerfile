#Is it necessary to make this?
#Dan says that this will essentially be the same as the dev stage.

FROM python:alpine as build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

ADD ./ /app/

#Change the RUN instruction
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN adduser -u 1234 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM python:alpine as prod

#COPY ?

EXPOSE 8080

#CMD
CMD ["python", "drf_jwt_backend/manage.py", "runserver", "0.0.0.0:8080"]