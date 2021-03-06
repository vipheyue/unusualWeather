# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /unusualWeather

# Copy the current directory contents into the container at /app
ADD . /unusualWeather

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt &&  pip install --upgrade https://github.com/celery/celery/tarball/master

# Make port 80 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV PATH /unusualWeather:$PATH

# Run app.py when the container launches
CMD ["/bin/uwsgi",uwsgi.ini"]

