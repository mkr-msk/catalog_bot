FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml ./

# Устанавливаем зависимости через uv
RUN uv pip install --system -r pyproject.toml

# Копируем весь код бота
COPY . .

# Команда запуска (переопределяется в docker-compose.yml)
CMD ["python", "main.py"]