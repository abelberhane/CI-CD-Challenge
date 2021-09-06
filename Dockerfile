FROM python:buster

WORKDIR /program

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9001

CMD ["python", "./application.py"]
