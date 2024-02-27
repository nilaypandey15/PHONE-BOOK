import sqlite3

def create_table():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            CellNumber TEXT NOT NULL,
            Email TEXT
        )
    ''')

    connection.commit()
    connection.close()

def insert_data(name, cell_number, email):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO contacts (Name, CellNumber, Email) VALUES (?, ?, ?)
    ''', (name, cell_number, email))

    connection.commit()
    connection.close()



def fetch_and_display_data():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM contacts
    ''')

    data = cursor.fetchall()

    for row in data:
        print(f"ID: {row[0]}, Name: {row[1]}, Cell#: {row[2]}, Email: {row[3]}")

    connection.close()

create_table()

insert_data("Akash Patel", "1234567890", "akash.patel@example.com")
insert_data("Priya Singh", "0987654321", "priya.singh@example.com"),
insert_data("Ravi Verma", "1112223333", "ravi.verma@example.com"),
insert_data("Bob Brown", "7777777777", "bob.brown@example.com")
insert_data("Charlie Davis", "9999999999", "charlie.davis@example.com")

fetch_and_display_data()