# Use an official Python runtime as a base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the working directory
COPY Pipfile /app/

# Install dependencies using pipenv
RUN pip install pipenv && pipenv install

# Copy the Django project into the container
COPY puddle /app/

# Expose the port on which Django runs (default is 8000)
EXPOSE 8000

# Command to run the Django application and perform migrations
CMD ["sh", "-c", "pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000"]
