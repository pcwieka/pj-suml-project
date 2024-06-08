FROM python:3.10-slim

COPY docker/model/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /model
COPY docker/model/flask_server.py /model/

EXPOSE 8001

CMD ["python", "flask_server.py"]
