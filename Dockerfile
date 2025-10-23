# Stage 1: Base build state
FROM python:3.12-slim-bookworm

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
RUN mkdir -p /apps/data

# Set the working directory
WORKDIR /apps

# Copy the Django project into the container
COPY . .

# Copy the requirements file and install dependencies
COPY requirements-prod.txt /apps
RUN pip install --upgrade pip \
     && pip install --no-cache-dir --require-hashes -r requirements-prod.txt

# Expose the port Django will run on
EXPOSE 8000/tcp

# Make entry file executable
RUN chmod +x  /apps/entrypoint.sh
 
# Start the appslication using Dev Server
CMD ["/apps/entrypoint.sh"]