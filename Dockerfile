FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6
COPY requirements.txt requirements.txt
RUN pip3 install --default-timeout=1000 -r requirements.txt
COPY . /app