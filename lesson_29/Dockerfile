FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . .

RUN chmod +x /app/wait-for-it.sh

# Устанавливаем переменную окружения для PYTHONPATH
ENV PYTHONPATH=/app

# Команда для запуска тестов
CMD ["/app/wait-for-it.sh", "db:5432", "--", "pytest", "test_my_aqa_docker_db.py"]
