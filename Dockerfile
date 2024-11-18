FROM python:3.12.4-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt install curl -y

ENTRYPOINT [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
COPY src . 

