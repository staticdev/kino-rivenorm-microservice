FROM python:3.6.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# install requirements
RUN pip install -r requirements.txt

EXPOSE 5000

# Run app.py when the container launches
CMD ["gunicorn", "__init__:create_app()", "-b", ":5000"]
