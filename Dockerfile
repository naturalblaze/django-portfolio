# Stage 1: Base build state
FROM python:3.12-slim AS build

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container
RUN mkdir -p /apps/data

# Set the working directory
WORKDIR /apps

# Copy the requirements file and install dependencies
COPY requirements-prod.txt /apps
RUN pip install --upgrade pip \
     && pip install --no-cache-dir --require-hashes -r requirements-prod.txt

# Stage 2: Production Stage
FROM python:3.12-slim

# Setup nonroot user and apps directory
RUN useradd -m -r appuser && \
  mkdir -p /apps/data && \
  chown -R appuser /apps

# Copy the Python dependencies from the builder stage
COPY --from=build /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

# Set the working directory inside the container
WORKDIR /apps

# Copy the Django project into the container
COPY --chown=appuser:appuser . .

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Switch to non-root user
USER appuser

# Expose the port Django will run on
EXPOSE 8080/tcp

# Make entry file executable
RUN chmod +x  /apps/entrypoint.sh
 
# Start the appslication using Dev Server
CMD ["/apps/entrypoint.sh"]