import pytest
from db_config import get_connection



@pytest.fixture(scope="module")
def db_connection():
    conn = get_connection()
    yield conn
    conn.close()

def test_insert_record(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO test_table (id, name) VALUES (1, 'John Doe')")
    db_connection.commit()
    cursor.close()
    print("Запис додано")

def test_select_record(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM test_table WHERE id = 1")
    record = cursor.fetchone()
    assert record is not None, "Запис не знайдено"
    cursor.close()

def test_update_record(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("UPDATE test_table SET name = 'Jane Doe' WHERE id = 1")
    db_connection.commit()
    cursor.close()
    print("Запис оновлено")

def test_delete_record(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM test_table WHERE id = 1")
    db_connection.commit()
    cursor.close()
    print("Запис видалено")
