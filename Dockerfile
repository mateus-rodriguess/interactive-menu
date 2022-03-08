FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Add entrypoint to the image
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# Used in wait-for-postgres.sh to connect to PostgreSQL
# Needs to be updated, repeats in docker-compose
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD 35b23jk5b
ENV POSTGRES_DB app

COPY . /code/
