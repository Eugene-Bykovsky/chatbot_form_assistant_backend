# Чат-бот для анкетирования незрячих и слабовидящих

Проект для хакатона «Яндекс Практикума»:  
**Доступная система анкетирования** через веб и Telegram с поддержкой голосового вывода.

## 🎯 Цель
Позволить незрячим и слабовидящим пользователям проходить анкеты с помощью:
- Голосового озвучивания вопросов (TTS)
- Простого и доступного интерфейса

## 🛠 Технологии
- **Backend**: Django + Django REST Framework
- **База данных**: SQLite (для демо), легко масштабируется до PostgreSQL
- **Голос**: Yandex SpeechKit (TTS/STT)
- **Фронтенд**: HTML/CSS (доступная веб-форма)

## 🚀 Запуск проекта

### 1. Клонируйте репозиторий
```bash
git clone 
cd accessible_survey
```

### 2. Создайте виртуальное окружение
```
python -m venv venv  
source venv/bin/activate  # Linux/macOS  
venv\Scripts\activate     # Windows
```

### 3. Установите зависимости
```
pip install -r requirements.txt
```

### 4. Выполните миграции
```
python manage.py migrate
```

### 5. Создайте тестовую форму
```
python manage.py create_test_form
```

### 6. Создайте суперпользователя (для админки)
```
python manage.py createsuperuser
```

### 7. Запустите сервер

```
python manage.py runserver
```

### 8. Откройте в браузере

Веб-форма: http://127.0.0.1:8000/form/1/  
Админка: http://127.0.0.1:8000/admin/  