# Step 1: Use an official Python image
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100

# Step 3: Set work directory
WORKDIR /app

# Step 4: Copy project files into container
COPY . /app

# Step 5: Install system dependencies (optional, useful for packages like numpy, scikit-learn)
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 6: Install Python dependencies
RUN pip install -r requirements.txt

# Step 7: Expose the default Streamlit port
EXPOSE 8501

# Step 8: Run the Streamlit app
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
