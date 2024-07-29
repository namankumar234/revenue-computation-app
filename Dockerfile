# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /App

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Copy the combined script to run all scripts
COPY run_all_scripts.py .

# Specify the command to run the combined script
CMD ["python", "run_all_scripts.py"]