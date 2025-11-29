import sqlite3

conection = sqlite3.connect("produc.db")
conection.execute('''
    CREATE TABLE IF NOT EXISTS produc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT not null,
    precio REAL not null)
''')


conection.commit()
conection.close()
