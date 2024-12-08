FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the Streamlit default port
EXPOSE 8501

# Command to run the Streamlit app with auto-reload
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.runOnSave", "true"]
