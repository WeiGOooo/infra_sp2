FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

EXPOSE 8000


CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]

LABEL author='weigo_for_practicum' version=2