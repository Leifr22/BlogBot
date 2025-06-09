# BlogBot

Тестовое задание: Telegram-бот для блога с API-админкой на FastAPI.

---

## 🔧 Стек

- **FastAPI** + SQLite  
- **Python Telegram Bot** (`telebot`)
- **SQLAlchemy ORM**
- `requests`, `python-dotenv`

---

## 🗂️ Структура проекта

```
BlogBot/
├── app/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── db_depends.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── router.py
│   ├── __init__.py
│   ├── bot.py  #Код тг бота
│   ├── main.py
│   └── schemas.py
├── .env
└── requirements.txt
```


---

## 🚀 Запуск проекта

1. **Клонируй репозиторий:**
    ```bash
    git clone https://github.com/yourname/blogbot.git
    cd blogbot
    ```
2. **Создай виртуальное окружение:**
   ```bash
    python -m venv .venv
    ```
2. **Установи зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Создай файл `.env` в корне:**
    ```bash
    BOT_TOKEN=your_token_here
    API_URL=http://localhost:8000
    ```

4. **Запусти API:**
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Запусти Telegram-бота:**
    ```bash
    python app/bot.py
    ```

---

## 🔍 Функционал

### Команда `/posts` в Telegram:
- Показывает заголовки постов
- При нажатии — текст и дата публикации

### Админка через API:
- `POST   /posts` — создать пост
- `GET    /posts` — список постов
- `GET    /posts/{id}` — детали поста
- `PUT    /posts/{id}` — обновить пост
- `DELETE /posts/{id}` — удалить пост

Документация доступна по адресу:  
[http://localhost:8000/docs](http://localhost:8000/docs)
