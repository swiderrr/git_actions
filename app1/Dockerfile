FROM python:3.10.5-slim
WORKDIR /app1
RUN apt-get update && apt-get install -y \
    curl apt-utils
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN addgroup --system docker && useradd --system --group docker duser
USER duser
CMD gunicorn --bind :8010 app1.wsgi --workers 1 --timeout 120