# rpi-core

Готовый скелет DevOps-сервиса для платформы Retail Pulse Index (RPI).

## Структура проекта

- `Dockerfile` — описание Docker-образа.
- `docker-compose.yml` — локальная развёртка.
- `app/` — простой HTTP-сервис.
- `.github/workflows/core-ci.yml` — CI для сборки и теста.

## Быстрый старт

```bash
docker-compose up --build
```

Сервис будет доступен по адресу `http://localhost:8000`.

## CI/CD

При пуше в ветку `main` автоматически запускается GitHub Actions, который собирает образ и выполняет smoke-тест.
