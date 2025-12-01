import sqlite3

conection = sqlite3.connect("produc.db")
#
#execute crea nuestra tabla
conection.execute('''
     -- creamos las estructuras de los campos
    CREATE TABLE IF NOT EXISTS produc (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- esto hace que cada vez que se ingrese un producto se "actualize" o auto incremente el id
    nombre TEXT not null,
    precio REAL not null)
''')


conection.commit() # commit guarda los cambios de mi tabla

conection.execute(
    # esta es la forma correcta de usar la sintaxis de SQL con python
    '''
    INSERT INTO produc (nombre, precio) -- dento de commillas el codigo sql
    VALUES(?, ?)
    ''',
    # fuera de las comillas mis operaciones de python
    ("lapiz", 25.50)
)
