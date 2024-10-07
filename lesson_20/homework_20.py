import psycopg2


connection = psycopg2.connect(
    database="my_hillel_db",
    user="bogdan kravchenko",
    password="123newdb",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        category_id SERIAL PRIMARY KEY,
        category_name VARCHAR(255) NOT NULL UNIQUE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL UNIQUE,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL,
        category_id INT,
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
    );
''')

# Data into categories table
cursor.execute('''
    INSERT INTO categories (category_name) VALUES
    ('Electronics'),
    ('Books'),
    ('Clothing')
    ON CONFLICT (category_name) DO NOTHING;
''')

# Data into products table
cursor.execute('''
    INSERT INTO products (product_name, description, price, category_id) VALUES
    ('Smartphone', 'A high-end smartphone', 699.99, 1),
    ('Laptop', 'A powerful laptop', 999.99, 1),
    ('Novel', 'A bestselling novel', 19.99, 2),
    ('T-Shirt', 'A stylish T-shirt', 29.99, 3)
    ON CONFLICT (product_name) DO NOTHING;
''')

connection.commit()

join_query = '''
    SELECT p.product_name, p.description, p.price, c.category_name
    FROM products p
    JOIN categories c ON p.category_id = c.category_id;
'''

cursor.execute(join_query)

results = cursor.fetchall()

# Print result in console
print("Product Name | Description | Price | Category Name")
print("---------------------------------------------------")
for row in results:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

# Connection
cursor.close()
connection.close()