import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()


def create_table_product():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
            name VARCHAR(50),
            price INT,
            image VARCHAR(300)
        )
    """)


def create_table_users():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT,
            full_name VARCHAR(100)
        )
    """)


def add_user(user_id, user_full_name):
    cursor.execute("""
        INSERT INTO users(id, full_name)
        VALUES (?, ?)
    """, (user_id, user_full_name))
    db.commit()


def get_users():
    users = cursor.execute("""
        SELECT * FROM users
    """)
    return users.fetchall()


def add_product_data(name, price, image):
    cursor.execute("""
        INSERT INTO product(name, price, image)
        VALUES (?, ?, ?)
    """, (name, price, image))
    db.commit()


def get_all_products():
    data = cursor.execute("""
        SELECT * FROM product
    """)
    return data.fetchall()


def delete_product(product_name):
    cursor.execute("""
        DELETE FROM product
        WHERE name = ?
    """, (product_name, ))
    db.commit()


def update_product(name, price, image):
    cursor.execute("""
        UPDATE product
        SET price = ?, image = ?
        WHERE name = ?
    """, (price, image, name))
    db.commit()