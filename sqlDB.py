import sqlite3

db = sqlite3.connect('Account.db')
cur = db.cursor()
    # Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    EMAIL TEXT,
    PASS TEXT
)""")

db.commit()

email = "join.ronin3412@gmail.com"
password = "Prokuror@228"

cur.execute(f"SELECT EMAIL FROM Account WHERE EMAIL = '{email}'")
if cur.fetchone() is None:
    cur.execute("""INSERT INTO Account(EMAIL, PASS) VALUES (?,?);""", (email, password))
    db.commit()
    print("Зарегистрированно!")
    for value in cur.execute("SELECT * FROM Account"):
        print(value)