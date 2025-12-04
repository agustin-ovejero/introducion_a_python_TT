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

def  dando_productos_por_comparacion(dato, dato_a_comparar):
    """Retornamos los productos de la base de datos que coinciden con la comparación"""
    if dato == 1:
        cursor.execute('SELECT * FROM productostp WHERE precio = ?', (dato_a_comparar,))
        los_datos = cursor.fetchall()
    elif dato == 2:
        cursor.execute('SELECT * FROM productostp WHERE precio >= ?', (dato_a_comparar,))
        los_datos = cursor.fetchall()
    elif dato == 3:
        cursor.execute('SELECT * FROM productostp WHERE precio <= ?', (dato_a_comparar,))
        los_datos = cursor.fetchall()
    for i in los_datos: 
        print(f"ID: {i[0]} | Nombre: {i[1]} | Descripción: {i[2]} | Cantidad: {i[3]} | Precio: {i[4]} | Categoria: {i[5]} ")
    print("\n")

def buscar_de_campos(dato, opcion):
    """Retornamos los productos de la base de datos que pertenescan a ciertos campos"""
    if dato == 1:
        cursor.execute('SELECT * FROM productostp WHERE id = ?', (opcion,))
        los_datos = cursor.fetchall()
    elif dato == 2:
        cursor.execute('SELECT * FROM productostp WHERE nombre = ?', (opcion,))
        los_datos = cursor.fetchall()
    elif dato == 3:
        cursor.execute('SELECT * FROM productostp WHERE categoria = ?', (opcion,))
        los_datos = cursor.fetchall()
    for i in los_datos: 
        print(f"ID: {i[0]} | Nombre: {i[1]} | Descripción: {i[2]} | Cantidad: {i[3]} | Precio: {i[4]} | Categoria: {i[5]} ")
    print("\n")
        

def eliminando_producto(dato):
    """Eliminamos productos de la base de datos por id"""
    try:
        cursor.execute('DELETE FROM productostp WHERE id = ?', (dato,))
        coneccion.commit()
    except Exception as e:
        print("algo salio mal", e)
        coneccion.rollback()
        coneccion.close()

def actualizar_producto(dato, nombre, descripcion, catidad, precio, categoria):
    """Actualizamos productos de la base de datos a trabes de un id"""
    try:
        coneccion.execute("""
            UPDATE productostp SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
            """, (nombre, descripcion, catidad, precio, categoria, dato)
        )
        coneccion.commit()
    except Exception:
        print("algo salio mal")
        coneccion.rollback()
        coneccion.close()
    
    
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    """Función que agrega productos a la base de datos"""
    try:
        coneccion.execute('''
            INSERT INTO productostp (nombre, descripcion, cantidad, precio, categoria) 
            VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria)
        )
        coneccion.commit()
    except Exception:
        print("algo salio mal")
        coneccion.rollback()
        coneccion.close()
        
        
def mostrar_productos():
    """Función que muestra los productos de la base de datos"""
    cursor.execute('SELECT * FROM productostp')
    datos = cursor.fetchall()
    for i in datos:
        print(f"ID: {i[0]} | Nombre: {i[1]} | Descripción: {i[2]} | Cantidad: {i[3]} | Precio: {i[4]} | Categoria: {i[5]} ")
    print("\n")
    
def eleccion(x): 
    """Devolvera la elección de preferencia del usuario, para mostar los productos de la base de datos"""
    if x == 1:
        try:
            dato_elegido = int(input("ingrese el id para buscar el producto: "))
            if dato_elegido == 0:
                raise ValueError
        except ValueError:
            print("dato invalido")
    elif x == 2:
        try:
            dato_elegido = input("ingrese el nombre para buscar el producto: ")
            if len(dato_elegido) == 0:
                raise ValueError
        except ValueError:
            print("dato invalido")
    elif x == 3:
        try:
            dato_elegido = input("ingrese la categoria para buscar los productos: ")
            if len(dato_elegido) == 0:
                raise ValueError
        except ValueError:
            print("dato invalido")
    return dato_elegido
        
        
    
    
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
6. Reporte de productos
7. Salir
"""
sub_menu_punto_cinco = """
1. Buscar por id
2. Buscar por nombre
3. Buscar por categoria
"""
sub_menu_punto_seis  = """
1. Igual a ...
2. Mayor a ...
3. Menor a ...
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
        agregar_producto(nombre, descripcion, catidad, precio, categoria)
        print("se agrego el producto correctamente", "\n")
        
    elif eligio == 2:
        print("Mostrando productos", "\n")
        mostrar_productos()
        
    elif eligio == 3:
        print("Mostrando productos", "\n")
        mostrar_productos()
        try:
            dato = int(input("elija la id a editar: "))
            if dato == 0:
                raise ValueError
        except ValueError:
            print("dato invalido")
        nombre, descripcion, catidad, precio, categoria = creacion_de_datos()
        actualizar_producto(dato, nombre, descripcion, catidad, precio, categoria)
        print("actualización completada")
    elif eligio == 4:    
        print("Mostrando productos", "\n")
        mostrar_productos()
        try:
            dato = int(input("elija la id a editar: "))
            if dato == 0:
                raise ValueError
        except ValueError:
            print("dato invalido")
        eliminando_producto(dato)
        print("producto eliminado")
    elif eligio == 5:
        mostrar_productos()
        print(sub_menu_punto_cinco)
        try:
            dato = int(input("elija la opcion: "))
        except ValueError:
            print("dato invalido")
        opcion = eleccion(dato)
        buscar_de_campos(dato, opcion)
        print("ejecución completada")
    elif eligio == 6:
        print(sub_menu_punto_seis)
        try:
            dato = int(input("elija la opcion: "))
        except ValueError:
            print("opción invalida")
        try:
            dato_a_comparar = float(input("ingrese el dato para comparar: "))
        except ValueError:
            print("opción invalida")
            
        dando_productos_por_comparacion(dato, dato_a_comparar)
        print("ejecución completada")
    elif eligio == 7: 
        continuo = 0
    else:
        print("Opcion invalida")
print("Adios") 
coneccion.close()
    