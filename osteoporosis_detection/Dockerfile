# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Start the server
CMD gunicorn osteoporosis.wsgi:application --bind 0.0.0.0:$PORT
