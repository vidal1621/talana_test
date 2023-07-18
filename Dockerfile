FROM ubuntu:latest
LABEL authors="cmendoza"
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]
# Path: talana_test/app.py
