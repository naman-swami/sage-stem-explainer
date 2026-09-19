# Sage STEM Domain Worker

This directory contains the custom OpenGAP Claw Worker for the Sage STEM Explainer project.

## Overview
The OpenGAP Domain Worker paradigm encapsulates specialized execution environments. This worker is tailored for the `Education / STEM` domain, focusing on generating step-by-step STEM concept explanations and validating math and physics units.

It implements a maker-checker workflow:
- **Maker (Sage)**: Breaks down the concept from first principles.
- **Checker (Reviewer)**: Validates mathematical correctness and explanation soundness.

## Files
- `worker.yaml`: The OpenGAP Claw Worker specification, defining memory bounds, tools, and execution contracts.
- `worker.py`: The daemon runtime orchestrating the maker-checker flow.
- `Dockerfile`: Production multi-stage Dockerfile for containerized deployments.
- `docker-compose.yml`: For local sandboxed execution.
- `deploy.sh`: Script to build and verify the worker locally.

## Security Envelope & Bounded Capabilities
The worker operates strictly within defined OpenGAP `securityConstraints`:
- `networkAccess`: Disabled.
- `fileSystemAccess`: Read/Write restricted to `/tmp/workspace`.
- Memory is bounded to 1024MB.

## Usage

### Local Testing
To test the script natively:
```bash
python worker.py --health
python worker.py --task '{"concept": "Thermodynamics", "audience_level": "Undergrad"}'
```

### Docker deployment
Build and deploy using the provided script:
```bash
chmod +x deploy.sh
./deploy.sh
```

### Docker Compose Sandbox
```bash
docker-compose up
```
