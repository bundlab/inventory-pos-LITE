FROM python:3.12-slim

WORKDIR /app

# Copy requirements from its actual location (backend/requirements.txt)
COPY backend/requirements.txt .

# Install (with timeout for Nigeria networks)
RUN pip install --no-cache-dir --default-timeout=120 -r requirements.txt

# Copy backend code from its actual location
COPY backend/app ./app

# Copy frontend build (this path is correct from root context)
COPY frontend/dist ./frontend/dist

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log", "--workers", "2"]
