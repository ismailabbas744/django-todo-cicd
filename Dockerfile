FROM python:3.9-slim

# Prevent Python from writing .pyc files and buffer logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /data

# Install Django directly as per your original design
RUN pip install --no-cache-dir django==3.2

COPY . .

EXPOSE 8000

# Run migrations and start server when the container boots up
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
