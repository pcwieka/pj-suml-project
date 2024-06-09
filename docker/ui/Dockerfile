FROM python:3.10-slim

RUN apt-get update && apt-get install -y build-essential

COPY docker/ui/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY ui /app/ui

EXPOSE 8501

CMD ["streamlit", "run", "ui/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
