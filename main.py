import os  # Librería de funciones de la consola de comandos


# Clase para los productos
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        # Atributos privados
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad

    # Getters para acceder a los atributos privados
    def get_nombre(self):
        return self._nombre

    def get_categoria(self):
        return self._categoria

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    # Setters para modificar los atributos, con validaciones
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_categoria(self, categoria):
        self._categoria = categoria

    def set_precio(self, precio):
        if precio <= 0:
            print("| !! El precio no puede ser negativo.")
            return
        self._precio = precio

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            print("| !! La cantidad no puede ser negativa.")
            return
        self._cantidad = cantidad


# Clase para el inventario
class Inventario:
    def __init__(self):
        self.productos = []  # Lista de productos
        self.cargar_productos() # Cargar productos desde el archivo al iniciar

    # Función para cargar los productos al inventario desde un archivo
    def cargar_productos(self):
        try:
            with open('inventario.txt', 'r') as archivo:
                for linea in archivo:
                    try:
                        # Dividir la línea en sus componentes
                        nombre, categoria, precio, cantidad = linea.strip().rsplit(',', 3)
                        producto = Producto(nombre, categoria, float(precio), int(cantidad))
                        self.productos.append(producto) # Añadir producto a la lista
                    except ValueError:
                        print(f"| !! Error en el formato de la línea: {linea.strip()}. Se ignorará.")
            print("Inventario cargado correctamente.")
        
        except FileNotFoundError:
            print("Archivo inventario.txt no encontrado. Se creará uno nuevo.")
            open('inventario.txt', 'w').close()  # Crear un nuevo archivo

    # Función para guardar el inventario en el archivo
    def guardar_inventario_en_archivo(self):
        try:
            with open('inventario.txt', 'w') as archivo:
                for producto in self.productos:
                    # Guardar cada producto en una nueva línea en el formato especificado
                    archivo.write(f"{producto.get_nombre()},{producto.get_categoria()},{producto.get_precio()},{producto.get_cantidad()}\n")
                print("El archivo de inventario se ha actualizado correctamente.")
        except Exception as e:
            print(f"|| Error al guardar el archivo: {e}")

    # Función para borrar la pantalla
    def borrar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Función para mostrar todo el inventario de productos
    def mostrar_inventario(self):
        print("\n" + "=" * 100)
        print("                Inventario de Productos")
        print("=" * 100)
        print(f"{'Nombre':<30} | {'Categoría':<20} | {'Precio':<10} | {'Cantidad':<10}")
        print("-" * 100)

        for producto in self.productos:
            print(f"{producto.get_nombre():<30} | {producto.get_categoria():<20} | "
                  f"{producto.get_precio():<10.2f} | {producto.get_cantidad():<10}")

        print("=" * 100)
        print("\nPresione Enter para volver al menú...")
        input()
        self.borrar_pantalla()

    # Función para agregar nuevos productos
    def agregar_producto(self):
        print("\n" + "=" * 100)
        print("                Agregar Producto")
        print("=" * 100)

        nombre = self.obtener_input_no_vacio("Nombre (puede incluir espacios): ")
        categoria = self.obtener_input_no_vacio("Categoría (puede incluir espacios): ")
        precio = self.obtener_precio_valido("Precio: ")
        cantidad = self.obtener_cantidad_valida("Cantidad: ")

        producto = Producto(nombre, categoria, precio, cantidad)
        self.productos.append(producto) # Añadir el nuevo producto a la lista
        print(f"|| El producto '{nombre}' ha sido agregado con éxito al inventario.")

    # Función para eliminar un producto del inventario
    def eliminar_producto(self):
        self.mostrar_inventario() # Mostrar el inventario antes de eliminar
        print("\n" + "=" * 100)
        print("                Eliminar Producto")
        print("=" * 100)

        producto_eliminado = input("Elija el nombre del producto que desea eliminar: ").strip()
        for producto in self.productos:
            if producto.get_nombre().lower() == producto_eliminado.lower():
                self.productos.remove(producto) # Eliminar el producto de la lista
                print(f"|| El producto '{producto_eliminado}' ha sido eliminado con éxito.")
                return
        
        print(f"|| El producto '{producto_eliminado}' no existe en el inventario.")

    # Función para buscar productos en el inventario
    def buscar_producto(self):
        buscar_producto = input("Buscar producto: ").strip()
        encontrados = []

        # Separar las palabras de búsqueda para realizar una búsqueda más flexible
        palabras_busqueda = [palabra.lower() for palabra in buscar_producto.split()]

        for producto in self.productos:
            nombre_producto = producto.get_nombre().lower()
            # Verificar si todas las palabras de búsqueda están en el nombre del producto
            if all(palabra in nombre_producto for palabra in palabras_busqueda):
                encontrados.append(producto)
        
        # Mostrar los productos encontrados o un mensaje si no se encuentran
        if encontrados:
            print("\nEncontrados:")
            for producto in encontrados:
                print(f"|| {producto.get_nombre()} | {producto.get_categoria()} | {producto.get_cantidad()} | {producto.get_precio()}")
            print("=" * 100)
        else:
            print(f"|| El producto '{buscar_producto}' no existe en el inventario.")

        print("\nPresione Enter para volver al menú...")
        input()
        self.borrar_pantalla()

    #Función para actualizar productos en el inventario
    def actualizar_producto(self):
        print("\n" + "=" * 100)
        print("                Actualizar Producto")
        print("=" * 100)

        producto_actualizar = self.obtener_input_no_vacio("Nombre del producto a actualizar (puede incluir espacios): ").strip()

        for producto in self.productos:
            if producto.get_nombre().lower() == producto_actualizar.lower():

                #  Pedir nuevos valores para actualizar, con opciones para dejar en blanco
                nuevo_nombre = input(f"Nuevo nombre (actual: {producto.get_nombre()}): ").strip()
                if not nuevo_nombre:
                    nuevo_nombre = producto.get_nombre()
                
                nueva_categoria = input(f"Nueva categoría (actual: {producto.get_categoria()}): ").strip()
                if not nueva_categoria:
                    nueva_categoria = producto.get_categoria()
                
                precio_nuevo = self.obtener_precio_valido(f"Nuevo precio (actual: {producto.get_precio()}): ", producto.get_precio())
                cantidad_nueva = self.obtener_cantidad_valida(f"Nueva cantidad (actual: {producto.get_cantidad()}): ", producto.get_cantidad())
                

                #Confirmación de la actualización del producto
                print("=" * 100)
                print ("\Datos del producto actualizados:")
                print(f"Nombre: {nuevo_nombre}")
                print(f"Categoría: {nueva_categoria}")
                print(f"Precio: {precio_nuevo}")
                print(f"Cantidad: {cantidad_nueva}")
                print("=" * 100)
                confirmar = input("¿Desea actualizar este producto? (s/n): ").strip().lower()

                if confirmar == "s":
                    # Aplicar los nuevos valores al producto
                    producto.set_nombre(nuevo_nombre)
                    producto.set_categoria(nueva_categoria)
                    producto.set_precio(precio_nuevo)
                    producto.set_cantidad(cantidad_nueva)

                    print(f"|| El producto '{nuevo_nombre}' ha sido actualizado con éxito.")
                else:
                    print("| !! La actualización ha sido cancelada.")
                
                return
        
        print(f"|| El producto '{producto_actualizar}' no existe en el inventario o no lo ha escrito correctamente.")


    # Función para obtener una entrada de usuario que no puede estar vacía
    def obtener_input_no_vacio(self, mensaje):
        while True:
            entrada = input(mensaje).strip()
            if entrada:
                return entrada
            print("| !! La entrada no puede estar vacía.")

    # Función para obtener un precio válido
    def obtener_precio_valido(self, mensaje, precio_actual=None):
        while True:
            precio = input(mensaje)
            if not precio and precio_actual is not None:  # Si no se ingresa nada, usar el precio actual
                return precio_actual
            try:
                precio = float(precio)
                if precio <= 0:
                    print("| !! El precio debe ser mayor que cero.")
                else:
                    return precio
            except ValueError:
                print("| !! El precio debe ser un número.")
            
    # Función para obtener una cantidad válida
    def obtener_cantidad_valida(self, mensaje, cantidad_actual=None):
        while True:
            cantidad = input(mensaje)
            if not cantidad and cantidad_actual is not None:  # Si no se ingresa nada, usar la cantidad actual
                return cantidad_actual
            try:
                cantidad = int(cantidad)
                if cantidad < 0:
                    print("| !! La cantidad no puede ser negativa.")
                else:
                    return cantidad
            except ValueError:
                print("| !! La cantidad debe ser un número.")
    

    # Menú del programa con diferentes opciones
    def mostrar_menu(self):
        print("\n" + "=" * 100)
        print("      📦  Bienvenido al Inventario de Productos  📦")
        print("=" * 100)
        print("1  | Agregar producto")
        print("2  | Eliminar producto")
        print("3  | Buscar producto")
        print("4  | Actualizar producto")
        print("5  | Mostrar inventario")
        print("6  | Salir")
        print("=" * 100)

    def run(self):
        self.menu_opcion = -1
        
        while self.menu_opcion != 6:
            self.mostrar_menu() # Mostrar menú de opciones
            opcion = input("Elija una opción (1-6): ")
            self.borrar_pantalla()

            if opcion.isdigit():
                self.menu_opcion = int(opcion)
                if 1 <= self.menu_opcion <= 6:
                    # Ejecutar la opción seleccionada
                    if self.menu_opcion == 1:
                        self.agregar_producto()
                    elif self.menu_opcion == 2:
                        self.eliminar_producto()
                    elif self.menu_opcion == 3:
                        self.buscar_producto()
                    elif self.menu_opcion == 4:
                        self.actualizar_producto()
                    elif self.menu_opcion == 5:
                        self.mostrar_inventario()
                else:
                    print("| !! Opción no válida, elija un número del 1 al 6.")
            else:
                print("| !! Opción no válida, debe ser un número.")

        # Guardar el inventario en el archivo al salir
        self.guardar_inventario_en_archivo()


# Hilo principal del programa y su carga
if __name__ == "__main__":
    inventario = Inventario()  # Crear una instancia de la clase Inventario
    inventario.run() # Iniciar el programa
