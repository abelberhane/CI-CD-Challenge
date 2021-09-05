FROM python:buster

WORKDIR /program

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/.

CMD ["python", "./application.py"]