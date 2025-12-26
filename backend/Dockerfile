FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml ./

# Устанавливаем зависимости через uv
RUN uv pip install --system -r pyproject.toml

# Копируем весь код приложения
COPY . .

# Порт Django
EXPOSE 8000

# Команда запуска (переопределяется в docker-compose.yml)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]