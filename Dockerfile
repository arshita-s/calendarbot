
# Import Python runtime and set up working directory
FROM python:3.8-slim


# Install any necessary dependencies
RUN pip3 install -r requirements.txt

RUN sed -i 's/80/8080/g' /etc/nginx/conf.d/default.conf
EXPOSE 8080

# Run app.py when the container launches
CMD ["python3", "app.py"]