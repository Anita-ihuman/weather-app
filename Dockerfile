# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

# Copy the rest of the application files to the container
COPY . .

# Expose port 5001 for Flask
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
