FROM python:3.8-slim

# Install dependencies
RUN pip install flask redis

# Copy application code
COPY main.py /main.py

# Set the working directory
WORKDIR /

# Run the application
CMD ["python", "main.py"]
