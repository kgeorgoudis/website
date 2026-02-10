Title: Getting Started with Container-Based Development
Date: 2026-02-05 14:30
Modified: 2026-02-05 14:30
Category: devops
Tags: docker, containers, development, tutorial
Slug: getting-started-containers
Author: Konstantinos Georgoudis
Summary: Learn how to leverage containers for consistent development environments and smoother deployments. This guide covers Docker basics and best practices for local development.

# Getting Started with Container-Based Development

Containers have revolutionized how we develop and deploy applications. By packaging an application with all its dependencies, containers ensure consistency across development, testing, and production environments. In this article, we'll explore the fundamentals of container-based development and why it matters.

## Why Containers?

Traditional development often suffers from the "works on my machine" problem. Different team members might have different versions of languages, libraries, or system dependencies installed. Containers solve this by:

- **Consistency**: Everyone runs the same environment
- **Isolation**: Projects don't interfere with each other
- **Portability**: Easy to move between local, staging, and production
- **Reproducibility**: Environment is defined as code

## Your First Container

Let's start with a simple Python application. Here's a basic Dockerfile:

```dockerfile
# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["python", "app.py"]
```

This Dockerfile defines a reproducible environment for your Python application. Let's break it down:

1. **Base Image**: We start with Python 3.12 slim image
2. **Working Directory**: All subsequent commands run in `/app`
3. **Dependencies**: We copy and install requirements first (caching optimization)
4. **Application Code**: Copy the rest of the application
5. **Port**: Expose the application port
6. **Command**: Define how to run the application

## Building and Running

Build your container:

```bash
docker build -t my-python-app:latest .
```

Run it:

```bash
docker run -p 8000:8000 my-python-app:latest
```

Your application is now running in an isolated container, accessible at `localhost:8000`.

## Docker Compose for Multi-Container Apps

Real applications often need multiple services (app, database, cache). Docker Compose makes this easy:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

Start everything with:

```bash
docker-compose up -d
```

## Best Practices

### 1. Use Specific Tags
Don't use `latest` in production. Pin specific versions:

```dockerfile
FROM python:3.12.1-slim
```

### 2. Multi-Stage Builds
Reduce image size by separating build and runtime:

```dockerfile
# Build stage
FROM python:3.12 AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
```

### 3. Security Scanning
Always scan images for vulnerabilities:

```bash
docker scan my-python-app:latest
```

### 4. Use .dockerignore
Exclude unnecessary files:

```
.git
.env
__pycache__
*.pyc
node_modules
```

## Conclusion

Containers are a fundamental tool in modern DevOps. They provide consistency, reproducibility, and portability that make development smoother and deployments more reliable. Start small with a single container, then grow into multi-service architectures with Docker Compose.

In future articles, we'll explore Kubernetes for container orchestration, CI/CD pipelines with containers, and advanced Docker networking.

## Further Reading

- [Docker Official Documentation](https://docs.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Container Security Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

---

*Have questions or experiences with containers? [Get in touch](/contact/) - I'd love to hear about your container journey!*

