FROM python:3.12-alpine
WORKDIR /app
COPY kalkulator.py .
CMD ["python", "kalkulator.py"]
