# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app3

# Copy the current directory contents into the container at /app
ADD . /app3

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 95

# Define environment variable
ENV NAME APP3 World

# Run app.py when the container launches
CMD ["python", "app3.py"]
