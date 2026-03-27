# 1. Тот же самый образ Python, что и для бэкенда
FROM python:3.12-slim

# 2. Рабочая папка для бота
WORKDIR /app

# 3. Настройки Python (без кэша и буферизации)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Копируем исходники
COPY . .

# 5. Заглушка: запускаем бесконечный процесс (tail -f /dev/null),
# чтобы контейнер бота просто "висел" и работал в фоне, пока мы не напишем настоящий код на aiogram.
CMD ["tail", "-f", "/dev/null"]
