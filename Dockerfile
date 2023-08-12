FROM python:3.10-buster
EXPOSE 8000
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--env-file=.env", "--port", "8000", "--reload"]
