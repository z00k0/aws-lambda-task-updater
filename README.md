# Тестовое задание

Скрипт на Python для обновления записей в PostgreSQL. Работает в AWS Lambda, которая активируется через AWS API gateway.

Для работы скрипта нужно заменить данные для подключения к БД:

```python
    DB_HOST = "db_host"
    DB_NAME = "db_name"
    DB_USER = "db_user"
    DB_PASSWORD = "db_password"
    # DB_PORT = "5432"
    TABLE_NAME = "tasks"
```

Также для работы AWS Lambda необходимо создать Layer и добавить в него архив `python.zip` (в архиве модуль psycopg2-binary).
