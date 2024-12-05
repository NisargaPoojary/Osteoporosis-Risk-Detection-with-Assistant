# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY osteoporosis_detection/requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files (entire project, including osteoporosis_detection)
COPY . .

# Collect static files
RUN python osteoporosis_detection/manage.py collectstatic --noinput  # Make sure to specify the correct path to manage.py

# Start the server
CMD gunicorn osteoporosis_detection.wsgi:application --bind 0.0.0.0:$PORT  # Specify the correct path for wsgi
