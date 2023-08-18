FROM python:3.10-buster


WORKDIR /app

COPY requirements.txt .

RUN pip install pandas==2.0.3
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["gunicorn", "run:app", "-w", "8", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]