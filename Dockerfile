# Application Dockerfile
FROM python:3.12-slim

WORKDIR /app
EXPOSE 8080

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin:${PATH}"

# Install dependencies first to cache them
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen
ENV PATH="/root/.local/bin:${PATH}"

# Copy the application
COPY . .

# Inject app_type specific commands

RUN uv tool install streamlit
CMD ["streamlit", "run", "proto_carbongpt/main.py", "--server.port", "8080"]

