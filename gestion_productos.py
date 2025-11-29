menu = """
1. Agregar producto
2. Mostrar porductos
3. Buscar productos
4. Eliminar producto
5. Salir
"""
productos = []

def actualizar_posiciones(nuestros_productos):
    if len(nuestros_productos) == 0:
        return None
    
    for i in range(len(nuestros_productos)):
        nuestros_productos[i][0] = i

def es_nada(x):
    if x == "":
        return True
    return False

def agregar_producto(nuestros_productos):
    nombre = input("Ingrese nombre del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    precio = input("Ingrese el precio del producto: ")
    

    if es_nada(nombre):
        print("tiene que ingresar el nombre")
        return None
    elif es_nada(categoria):
        print("tiene que ingresar la categoria")
        return None
    elif es_nada(precio):
        print("tiene que ingresar el precio")
        return None

    if int(precio) < 0:
        print("tiene que ingresar un precio valido que sea mayor que cero")
        return None

    if len(nuestros_productos) == 0:
        producto = [0, nombre, categoria, int(precio)]
        nuestros_productos.append(producto)
        return 1
    else:
        producto = [(len(nuestros_productos) + 1) - 1, nombre, categoria, int(precio)]
        nuestros_productos.append(producto)
        return 1

def mostrar_productos(nuestros_productos):
    if len(nuestros_productos) == 0:
        print(nuestros_productos)
    
    for i in nuestros_productos:
        print(f"indentificación: {i[0]} | nombre: {i[1]} | categoria: {i[2]} | precio: {i[3]}")

def buscar_productos(nuestros_productos):
    producto = input("ingrese el producto a buscar: ")
    if es_nada(producto):
        print("tiene que ingresar un producto a buscar")
        return -1
    
    if len(nuestros_productos) == 0:
        return None
    
    contador = 0
    for i in nuestros_productos:
        if producto == i[1]:
            contador += 1
            print(f"indentificación: {i[0]}| nombre: {i[1]} | categoria: {i[2]} | precio: {i[3]}")
    
    if contador == 0:
        return None
    return 1

def eliminar_producto(nuestros_productos):
    if len(nuestros_productos) == 0:
        return None
    posicion = input("ingrese la posición del producto a eliminar: ")
    if es_nada(posicion):
        print("tiene que ingresar la posición del producto a eliminar")
        return None
    posicion = int(posicion)
    if posicion < 0 or posicion > len(nuestros_productos) -1:
        print("posición invalida")
        return None
    
    nuestros_productos.pop(posicion)
    actualizar_posiciones(nuestros_productos)

    return 1
    
def main():
    print(menu)
    eleccion = input()
    while eleccion != "5":
        mensaje = None
        #muestra resultado

        if eleccion == "1":
            condicionante = agregar_producto(productos)
            if condicionante is None:
                mensaje = "no se pudo agregar ningun producto"
            else:
                mensaje = "Se agrego el producto correctamente"
        elif eleccion == "2":
            print("Mostrando productos:")
            mostrar_productos(productos)
        elif eleccion == "3":
            condicionante = buscar_productos(productos)
            if condicionante is None:
                mensaje = "No se encontraron resultados"
            elif condicionante == -1:
                mensaje = "No se ha podido concretar la busqueda"
        elif eleccion == "4":
            condicionante = eliminar_producto(productos)
            if condicionante is None:
                mensaje = "No se pudo eliminar ningun producto"
            else:
                mensaje = "Producto eliminado"
        
        if mensaje is not None:
            print(mensaje)
            print()
        print(menu)
        eleccion = input()
        print()
    print("saliendo del sistema...")

main()