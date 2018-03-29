FROM python:3.5.4-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# install requirements
RUN pip install -r requirements.txt

EXPOSE 5000

# Run app.py when the container launches
CMD ["gunicorn", "app:APP", "-b", ":5000"]
