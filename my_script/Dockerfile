FROM python:3.13-rc-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install virtualenv

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

COPY . .

CMD ["python", "index.py"]