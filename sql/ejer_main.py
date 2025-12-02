import sqlite3
ejecutable = sqlite3.connect("productos.db")
cursor = ejecutable.cursor()

def validacion_int(x):
    try:
        dato = int(input(f"{x}: "))
        return dato
    except ValueError:
        print("dato invalido")
        return None
        
def validacion_str(x):
    try:
        dato = str(input(f"{x}: "))
        return dato
    except ValueError:
        print("dato invalido")
        return None
        
def cargar_productos(x, y):
    ejecutable.execute('''
        INSERT INTO productos (nombre, precio) VALUES (?, ?)
        ''',
        (x, y)
    )
    
def mostrar_db():
    cursor.execute('SELECT * FROM productos')
    mis_productos = cursor.fetchall()
    for i in mis_productos:
        print(f"ID {i[0]}, Nombre {i[1]}, Precio {i[2]} ")
     
para_elec = "ingrese eleción"
para_num = "ingrese precio"
par_nom = "ingrese nombre"
condicion = 1

menu = """
1. Ingresar producto
2. Mostrar Productos
3. Salir
"""
while condicion:
    print(menu)
    eleccion = validacion_int(para_elec)
    if eleccion == 1:
        nombre = validacion_str(par_nom)
        precio = validacion_int(para_num)
        cargar_productos(nombre, precio)
    elif eleccion == 2: 
        mostrar_db()
    elif eleccion == 3:
        condicion = 0
    else:
        print("elecion invalida")
print("adios") 
ejecutable.commit()
ejecutable.close()
    


