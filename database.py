import mysql.connector
DB_HOST = "db"  # 'db' se for local com docker-compose, 'localhost' em produção
DB_USER = "rafael"
DB_PASS = "aptdw"
DB_NAME = "mydb"


def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
        )
