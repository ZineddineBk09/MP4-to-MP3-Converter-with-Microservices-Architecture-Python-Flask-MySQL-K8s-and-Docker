FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential pkg-config \
  && pip install --no-cache-dir --upgrade pip 

# Set the working directory in the container
WORKDIR /app


COPY ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app 

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable

# Run the server
CMD ["python3", "server.py"]
