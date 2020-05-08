
# Import Python runtime and set up working directory
FROM python:3.8-slim
WORKDIR /app
ADD . /app

# Install any necessary dependencies
RUN pip3 install -r requirements.txt


# Run app.py when the container launches
CMD ["python3", "app.py"]