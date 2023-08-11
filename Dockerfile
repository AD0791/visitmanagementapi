FROM 3.12.0rc1-alpine3.18
EXPOSE 8000
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["uvicorn", "app.main:server", "--host", "0.0.0.0", "--env-file=.env", "--port", "8000", "--reload"]
