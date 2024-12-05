# Use the official Python image
FROM python:3.9-slim

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY osteoporosis_detection/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files (entire project, including osteoporosis_detection)
COPY . .

# Collect static files
RUN python osteoporosis_detection/manage.py collectstatic --noinput

# Start the server
CMD gunicorn osteoporosis_detection.wsgi:application --bind 0.0.0.0:$PORT
