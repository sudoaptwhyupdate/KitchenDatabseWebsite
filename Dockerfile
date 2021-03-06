# Set base image (host OS)
FROM python:3.8-slim

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /KitchenDatabseWebsite

# Copy the dependencies file to the working directory
COPY requirements.txt .

COPY JSrequirements.txt .

# Install any dependencies
RUN python3 -m pip install -r requirements.txt

RUN mpn install JSrequirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python3", "./app.py" ]