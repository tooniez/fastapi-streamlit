# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /api

# Copy the requirements file into the container
COPY api /api

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]