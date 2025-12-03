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


menu = """
1. Registrar nuevos productos
2. Ver Productos
3. Actualizar productos
4. Eliminar Productos
5. Busccar producto
"""
sub_menu_punto_cinco = """
1. Buscar por id
2. Buscar por nombre
3. Buscar por categoria
"""
continuo = 1
while continuo:
    print(menu)
    try:
        eligio = int(input(": "))
    except ValueError:
        print("dato invalido")
    
    if eligio == 1:
        print("queso")
    elif eligio == 2:
        print("queso")
    elif eligio == 3:
        print("queso")
    elif eligio == 4:    
        print("queso")
    elif eligio == 5:
        print("queso")
    else:
        print("Opcion invalida")
        
    