FROM python:3.10.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

# Copy the requirements directory to the container
COPY ./requirements /usr/src/app/requirements

# Install project dependencies from dev.txt
RUN pip install -r requirements/dev.txt

# Copy the entrypoint script to the container
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

RUN chmod +x /usr/src/app/entrypoint.sh

# Copy your Django project code into the container
COPY . /usr/src/app

# Set the entrypoint command
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
