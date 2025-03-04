# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a mounting point for flow of data
VOLUME ["app/input_data.csv", "app/output_data.csv"] 

# Install the Python dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "etl.py"]
