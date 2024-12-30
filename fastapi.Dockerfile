FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app
WORKDIR /app

RUN uv sync --frozen --no-cache

CMD ["uv", "run", "fastapi", "run", "backend/main.py", "--port", "80", "--host", "0.0.0.0"]

