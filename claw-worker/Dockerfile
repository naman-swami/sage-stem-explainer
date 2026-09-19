# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app
COPY worker.py .
COPY worker.yaml .

# Compile Python byte code
RUN python -m py_compile worker.py

# Stage 2: Runtime
FROM python:3.11-slim

# Create a non-root user
RUN useradd -m worker
USER worker
WORKDIR /app

# Copy from builder
COPY --from=builder /app /app

ENTRYPOINT ["python", "worker.py"]
CMD ["--health"]
