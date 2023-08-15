FROM python:3.11-slim-buster
EXPOSE 8000
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--env-file=.env", "--port", "8000", "--reload"]
