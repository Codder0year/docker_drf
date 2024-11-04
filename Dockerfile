FROM python:3.12-slim

# Устанавливаем зависимости для Poetry и запуска приложения
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями Poetry (pyproject.toml и poetry.lock)
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости через Poetry
RUN ~/.local/bin/poetry config virtualenvs.create false && \
    ~/.local/bin/poetry install --no-dev

# Копируем весь проект в контейнер
COPY . /app

# Указываем команду по умолчанию для контейнера в docker-compose.yaml