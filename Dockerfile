# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8505


# Run the application
ENTRYPOINT ["streamlit", "run"]
CMD ["malaria_web_app.py", "--server.port=8505"]
