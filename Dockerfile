FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app

COPY pyproject.toml uv.lock /app/

RUN uv sync --locked

COPY . /app/

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev", "--host", "0.0.0.0", "--port", "8000"]