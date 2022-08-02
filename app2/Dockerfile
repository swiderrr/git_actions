FROM python:3.10.5-slim
WORKDIR /app2
RUN apt-get update && apt-get install -y \
    curl apt-utils
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
ADD start.sh /
RUN addgroup --system docker && useradd --system --group docker duser && chmod +x /start.sh
USER duser
CMD ["/start.sh"]
