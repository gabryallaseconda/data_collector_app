FROM python:3.6.5
# Set the working directory to /app
WORKDIR /app
# Copy local contents into the container
ADD . /app
# Install all required dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]


#FROM rabbitmq:3-management
#ENV RABBITMQ_ERLANG_COOKIE "SWQOKODSQALRPCLNMEQG"
#ENV RABBITMQ_DEFAULT_USER "rabbitmq"
#ENV RABBITMQ_DEFAULT_PASS "rabbitmq"
#ENV RABBITMQ_DEFAULT_VHOST "/"
