# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the dashboard
CMD ["python", "dashboard/app.py"]