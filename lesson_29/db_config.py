import psycopg2
from psycopg2 import sql

def get_connection():
    return psycopg2.connect(
        dbname="aqa_hillel_docker_test_db",
        user="aqa_hillel_user",
        password="test_password",
        host="db",
        port="5432"
    )