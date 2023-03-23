import json
import psycopg2


def lambda_handler(event, context):
    DB_HOST = "db_host"
    DB_NAME = "db_name"
    DB_USER = "db_user"
    DB_PASSWORD = "db_password"
    # DB_PORT = "5432"
    TABLE_NAME = "tasks"

    task_fields = [
        "name",
        "status",
        "item",
        "brand",
        "category",
        "outcome",
        "assignee",
    ]

    task_id = event.get("id")
    columns = []
    values = []
    for key, value in event.items():
        if key in task_fields:
            columns.append(key)
            values.append(value)
    record = ", ".join([f"{col}=%s" for col in columns])
    sql = f"UPDATE {TABLE_NAME} SET {record} WHERE id=%s"

    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        # port=DB_PORT,
    )
    with conn.cursor() as cur:
        cur.execute(sql, values + [task_id])
        conn.commit()
    conn.close()
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(
            {
                "Task updated": event,
            }
        ),
        "isBase64Encoded": False,
    }
