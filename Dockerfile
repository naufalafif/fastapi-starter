FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
COPY ./app/requirements.txt requirements.txt
RUN pip3 install --default-timeout=1000 -r requirements.txt
COPY ./app /app
ENV PYTHONPATH=/app