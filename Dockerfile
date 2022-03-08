FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Add entrypoint to the image
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . /code/
