import sqlite3

conection = sqlite3.connect("produc.db")
# conection y cursor no son lo mismo. 
#cursor tinee pinta que solamente hace nuestras consultas SQL 

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
conection.commit()

cursor = conection.cursor() # Para poder recibir los datos de mi tabla es necesario crear un cursor de mi coneción original y esta es la forma
cursor.execute('SELECT * FROM produc')
productos = cursor.fetchall()# con fetchall conseguimos los datos
#print(productos)
# for producto in productos:
#     print(f"ID: {producto[0]} Nombre: {producto[1]}, Precio: {producto[2]} ")

# ejemplo de actulaizacioón con UPDATE
nuevo_precio = 250.0
id_producto = 1
cursor.execute('UPDATE produc SET precio = ? WHERE id = ?', (nuevo_precio, id_producto))
conection.commit()

cursor.execute('SELECT * FROM produc')
productos = cursor.fetchall()
# for producto in productos:
#     print(f"ID: {producto[0]} Nombre: {producto[1]}, Precio: {producto[2]} ")
    
    
# Delete en SQL    
# SIEMPRE USAR WHERE CUANDO USAMO DELETE
id = 2
cursor.execute('DELETE FROM produc WHERE id = ?', (id,))
conection.commit()
cursor.execute('SELECT * FROM produc')
productos = cursor.fetchall()
for producto in productos:
     print(f"ID: {producto[0]} Nombre: {producto[1]}, Precio: {producto[2]} ")