FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

# EXPOSE 80
EXPOSE 8080

# CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]