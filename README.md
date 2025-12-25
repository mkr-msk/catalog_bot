# Catalog Bot

Telegram-бот каталог с приёмом заявок для малого бизнеса.

## Описание

Бот позволяет:
- Просматривать товары/услуги по категориям
- Видеть описание и цену
- Оставлять заявку (имя, телефон, комментарий)
- Владелец получает уведомления о новых заявках

Управление товарами через Django Admin панель.

## Технологии

- **Backend:** Django 5.x, Django REST Framework
- **Bot:** aiogram 3.x
- **Database:** PostgreSQL 16
- **Containerization:** Docker, Docker Compose
- **Package Manager:** uv

## Структура проекта
```
catalog_bot/
├── backend/     # Django приложение
├── bot/         # Telegram bot
├── docker-compose.yml
└── README.md
```

## Разработка

_(будет дополнено при настройке окружения)_

## Деплой

_(будет дополнено)_