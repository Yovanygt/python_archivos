import os

# Estructura para almacenar detalles de productos
class Producto:
    def __init__(self):
        self.codigo = ""
        self.nombre = ""
        self.precio = 0.0
        self.proveedor = ""
        self.existencia = 0
        self.estado = ""
        self.descuento = 0.0

# Función para mostrar el menú de opciones al usuario
def menus():
    while True:
        print("     << MENU PRODUCTOS DE LA TERMINAL  >>     ")
        print("  1. Agregar Producto")
        print("  2. Buscar Producto")
        print("  3. Editar Producto")
        print("  4. Salir Del Programa\n")
        try:
            x = int(input("Elija una Opcion: "))
            if 1 <= x <= 4:
                return x
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            
# Función para verificar si un código de producto ya existe en el archivo
def verifica(codigo):
    try:
        with open("Productos.txt", "r") as leer:
            for line in leer:
                codigoLeido = line.split()[0]
                if codigoLeido == codigo:
                    print("Este código ya existe\n\n\n")
                    return False
        return True
    except FileNotFoundError:
        return True
    
# Función para agregar un nuevo producto
def agregar_producto():
    os.system("cls" if os.name == "nt" else "clear")
    producto = Producto()

    with open("Productos.txt", "a") as es:
        producto.codigo = input("Código del producto: ")
        if verifica(producto.codigo):
            producto.nombre = input("Nombre del Producto: ")
            producto.precio = float(input("Precio: "))
            producto.proveedor = input("Proveedor: ")
            producto.existencia = int(input("Existencias del producto: "))
            producto.estado = input("Estado del Producto (A = Aprobado, R = Reprobado): ")
            producto.descuento = float(input("Descuento del Producto: "))

            es.write(f"{producto.codigo} {producto.nombre} {producto.precio:.2f} {producto.proveedor} {producto.existencia} {producto.estado} {producto.descuento:.2f}\n")

            print("El producto se ha agregado exitosamente.")

# Función para buscar un producto por su código
def buscar_producto(codigo):
    try:
        with open("Productos.txt", "r") as leer:
            encontrado = False
            for line in leer:
                data = line.split()
                producto = Producto()
                producto.codigo, producto.nombre, producto.precio, producto.proveedor, producto.existencia, producto.estado, producto.descuento = data

                if producto.codigo == codigo:
                    encontrado = True
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Producto encontrado:")
                    print(f"Código: {producto.codigo}")
                    print(f"Nombre: {producto.nombre}")
                    print(f"Precio: {float(producto.precio):.2f}")
                    print(f"Proveedor: {producto.proveedor}")
                    print(f"Existencias: {int(producto.existencia)}")
                    print(f"Estado: {producto.estado}")
                    print(f"Descuento: {float(producto.descuento):.2f}\n\n\n")
                    break
            if not encontrado:
                print("Producto no encontrado.")
    except FileNotFoundError:
        print("El archivo 'Productos.txt' no existe o está vacío.")

# Función para editar un producto existente
def editar_producto():
    os.system("cls" if os.name == "nt" else "clear")
    codigoEditar = input("Editar Producto\nIngrese el código del producto a editar: ")

    try:
        with open("Productos.txt", "r") as leer, open("temp.txt", "w") as temp:
            encontrado = False
            for line in leer:
                data = line.split()
                producto = Producto()
                producto.codigo, producto.nombre, producto.precio, producto.proveedor, producto.existencia, producto.estado, producto.descuento = data

                if producto.codigo == codigoEditar:
                    encontrado = True
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Producto actual:")
                    print(f"Código: {producto.codigo}")
                    print(f"Nombre: {producto.nombre}")
                    print(f"Precio: {float(producto.precio):.2f}")
                    print(f"Proveedor: {producto.proveedor}")
                    print(f"Existencias: {int(producto.existencia)}")
                    print(f"Estado: {producto.estado}")
                    print(f"Descuento: {float(producto.descuento):.2f}\n")

                    print("Ingrese los nuevos datos:")
                    producto.nombre = input("Nombre del Producto: ")
                    producto.precio = float(input("Precio: "))
                    producto.proveedor = input("Proveedor: ")
                    producto.existencia = int(input("Existencias del producto: "))
                    producto.estado = input("Estado del Producto (A = Aprobado, R = Reprobado): ")
                    producto.descuento = float(input("Descuento del Producto: "))

                temp.write(f"{producto.codigo} {producto.nombre} {producto.precio:.2f} {producto.proveedor} {producto.existencia} {producto.estado} {producto.descuento:.2f}\n")

            if not encontrado:
                print("Producto no encontrado.")

        os.remove("Productos.txt")
        os.rename("temp.txt", "Productos.txt")
    except FileNotFoundError:
        print("El archivo 'Productos.txt' no existe o está vacío.")

if __name__ == "__main__":
    while True:

        # Mostrar el menú y obtener la elección del usuario
        op = menus()

        # Comprobar la elección del usuario
        if op == 1:
            print("Agregar un Producto")
            agregar_producto() # Llamar a la función para agregar un producto
        elif op == 2:
            print("Buscar Producto")
            codigo = input("Ingrese el código del producto a buscar: ")
            buscar_producto(codigo) # Llamar a la función para agregar un producto
        elif op == 3:
            editar_producto() # Llamar a la función para editar un producto
        elif op == 4:
            break # Salir del bucle y finalizar el programa
