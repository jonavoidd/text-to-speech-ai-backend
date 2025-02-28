# Use a base image with ffmpeg pre-installed
FROM jrottenberg/ffmpeg:4.4-ubuntu

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY ./app /app

# Expose FastAPI port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]