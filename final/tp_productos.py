import sqlite3

coneccion = sqlite3.connect("inventario.db")
cursor = coneccion.cursor()

coneccion.execute('''
    CREATE TABLE IF NOT EXISTS productostp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL
    )
    ''')
