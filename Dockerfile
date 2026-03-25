# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app


# Copy dependency file first (leverages Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run as a non-root user for security
RUN useradd --create-home appuser
USER appuser

# Start the application
CMD ["python", "app.py"]
