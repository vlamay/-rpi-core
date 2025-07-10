FROM python:3.11-slim

WORKDIR /usr/src/app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000
CMD ["python", "app/main.py"]