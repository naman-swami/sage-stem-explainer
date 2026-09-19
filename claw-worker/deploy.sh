#!/bin/bash
set -e

echo "Deploying Sage STEM Domain Worker..."

# Build Docker image
echo "Building Docker image..."
docker build -t sage-stem-domain-worker:latest .

# Run healthcheck
echo "Running healthcheck..."
HEALTH=$(docker run --rm sage-stem-domain-worker:latest --health)

if [[ "$HEALTH" == *"\"status\": \"ok\""* ]]; then
    echo "Healthcheck passed: $HEALTH"
else
    echo "Healthcheck failed!"
    exit 1
fi

echo "Deployment successful."
