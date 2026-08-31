FROM python:3.12-alpine

WORKDIR /app

RUN apk update && apk upgrade

COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ backend/

EXPOSE 5000

CMD ["python", "-m", "backend.app"]
