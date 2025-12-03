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

def dar_nombre():
    """Validara y retornara el nombre del producto"""
    try:
        dato = input("ingrese el nombre: ")
        if len(dato) == 0:
            raise ValueError
    except ValueError:
        print("Dato ingresado invalido")
    return dato

def dar_descripcion():
    """Validara y retornara la descripción del producto"""
    
    try:
         dato = input("ingrese la descripción: ")
         if len(dato) == 0:
             raise ValueError
    except ValueError:
         print("Dato ingresado invalido")
    return dato
    
def dar_cantidad():    
    """Validara y retornara la cantidad del producto"""
        
    try:
         dato = int(input("ingrese la cantidad: "))
         if dato == 0:
             raise ValueError
    except ValueError:
         print("Dato ingresado invalido")
    return dato

def dar_precio():
    """Validara y retornara el precio del producto"""
            
    try:
         dato = int(input("ingrese el precio: "))
         if dato == 0:
             raise ValueError
    except ValueError:
         print("Dato ingresado invalido")
    return dato
    
def dar_categoria():
    """Validara y retornara la categoria del producto"""
                
    try:
         dato = input("ingrese la categoria: ")
         if len(dato) == 0:
             raise ValueError
    except ValueError:
         print("Dato ingresado invalido")
    return dato
    

def creacion_de_datos():
    """
    Funcion que retornara el nombre, descripción, cantidad, precio y categoria
    para la creación de un producto
    """
    nombre = dar_nombre()
    descripcion = dar_descripcion()
    cantidad = dar_cantidad()
    precio = dar_precio()
    categori = dar_categoria()
    return (nombre, descripcion, cantidad, precio, categori)

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
        nombre, descripcion, catidad, precio, categoria = creacion_de_datos()
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
        
    