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
├── backend/              # Django приложение
│   ├── catalog/         # Основное приложение
│   ├── config/          # Настройки Django
│   ├── manage.py
│   └── Dockerfile
├── bot/                 # Telegram bot
│   ├── handlers/        # Обработчики команд
│   ├── keyboards/       # Клавиатуры
│   ├── utils/           # API клиент
│   ├── main.py
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone <your-repo-url>
cd catalog_bot
```

### 2. Настройте окружение

Скопируйте `.env.example` в `.env` и заполните:
```bash
cp .env.example .env
```

Получите токен бота от [@BotFather](https://t.me/botfather) и ваш Telegram ID от [@userinfobot](https://t.me/userinfobot).

Отредактируйте `.env`:
```env
BOT_TOKEN=ваш_токен_от_botfather
ADMIN_TELEGRAM_ID=ваш_telegram_id
SECRET_KEY=сгенерируйте_случайный_ключ
```

### 3. Запустите проект
```bash
docker-compose up -d
```

### 4. Примените миграции
```bash
docker-compose exec backend python manage.py migrate
```

### 5. Создайте суперпользователя
```bash
docker-compose exec backend python manage.py createsuperuser
```

### 6. Откройте админку

Перейдите на http://localhost:8000/admin и войдите с созданными данными.

Добавьте категории и товары через админ-панель.

### 7. Протестируйте бота

Найдите вашего бота в Telegram и отправьте `/start`.

## Команды для разработки
```bash
# Просмотр логов
docker-compose logs -f

# Перезапуск сервисов
docker-compose restart backend bot

# Остановка
docker-compose down

# Пересборка образов
docker-compose up --build
```

## API Endpoints

- `GET /api/categories/` - список категорий
- `GET /api/products/` - список товаров
- `GET /api/products/{id}/` - детали товара
- `GET /api/products/by-category/{category_id}/` - товары категории
- `POST /api/orders/` - создание заявки

## Лицензия

Проект для портфолио