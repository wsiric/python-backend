# FROM python:3.10

# WORKDIR /app

# COPY app/pop.csv /app/pop.csv
# COPY requirements.txt requirements.txt

# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
# RUN pip3 install Flask gunicorn

# COPY app/ /app/

# ENV PORT 5000

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app


FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./app.py