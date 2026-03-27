# 1. Берем за основу готовую легкую версию Linux с Python 3.12
FROM python:3.12-slim

# 2. Указываем, что внутри контейнера вся работа будет идти в папке /app
WORKDIR /app

# 3. Настройки Python: отключаем создание мусорных файлов кэша (.pyc) и буферизацию
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Сначала копируем только списки зависимостей
COPY requirements.txt .

# 5. Устанавливаем все библиотеки для Django
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем весь остальной наш код бэкенда внутрь контейнера
COPY . .

# 7. Эта команда автоматически запустится при запуске контейнера (включаем сервер)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
