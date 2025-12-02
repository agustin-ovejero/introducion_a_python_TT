import sqlite3
conecxion = sqlite3.connect("productos.db")
conecxion.execute('''
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL)
    
    ''')
conecxion.commit()
conecxion.close()