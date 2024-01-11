FROM python:3.13-rc-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install virtualenv

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

COPY . .

ARG DEFAULT_PORT 5000

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

CMD ["python", "-m" ,"flask", "--app", "hello", "run" , "--host=0.0.0.0"]