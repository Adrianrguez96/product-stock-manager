import os  # Librería de funciones de la consola de comandos


# Clase para los productos
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        """
        Inicializa un nuevo producto.

        :param nombre: Nombre del producto.
        :param categoria: Categoría del producto.
        :param precio: Precio del producto (debe ser mayor que 0).
        :param cantidad: Cantidad del producto (debe ser mayor o igual que 0).
        """

        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
    
    def __str__ (self):
        return f"{self._nombre:<30} | {self._categoria:<20} | {self._precio:<10.2f} | {self._cantidad:<10}"

    # Getters para acceder a los atributos privados
    def get_nombre(self):
        """Retorna el nombre del producto."""
        return self._nombre

    def get_categoria(self):
        """Retorna la categoria del producto."""
        return self._categoria

    def get_precio(self):
        """Retorna el precio del producto."""
        return self._precio

    def get_cantidad(self):
        """Retorna la cantidad del producto."""
        return self._cantidad

    # Setters para modificar los atributos, con validaciones
    def set_nombre(self, nombre):
        """Establece el nombre del producto."""
        self._nombre = nombre

    def set_categoria(self, categoria):
        """Establece el nombre de la categoria."""
        self._categoria = categoria

    def set_precio(self, precio):
        """Establece el precio del producto, validando que sea mayor que 0."""
        if precio <= 0:
            print("| !! El precio no puede ser negativo o cero.")
            return
        self._precio = precio

    def set_cantidad(self, cantidad):
        """Establece la cantidad del producto, validando que no sea negativa."""
        if cantidad < 0:
            print("| !! La cantidad no puede ser negativa.")
            return
        self._cantidad = cantidad


# Clase para el inventario
class Inventario:

    def __init__(self):
        """Inicializa el inventario y carga los productos desde un archivo."""
        self.productos = []  # Lista de productos
        self.cargar_productos() # Cargar productos desde el archivo al iniciar

    def cargar_productos(self):
        """Carga los productos desde el archivo 'inventario.txt'."""
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

    def guardar_inventario_en_archivo(self):
        """Guarda el inventario en el archivo 'inventario.txt'."""
        try:
            with open('inventario.txt', 'w') as archivo:
                for producto in self.productos:
                    # Guardar cada producto en una nueva línea en el formato especificado
                    archivo.write(f"{producto.get_nombre()},{producto.get_categoria()},{producto.get_precio()},{producto.get_cantidad()}\n")
                print("El archivo de inventario se ha actualizado correctamente.")
        except Exception as e:
            print(f"|| Error al guardar el archivo: {e}")

    def borrar_pantalla(self):
        """Borra la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def modo_espera(self):
        """Pone el programa en modo espera hasta que el usuario presione Enter."""
        print("\nPresione Enter para volver al menú...")
        input()
        self.borrar_pantalla()

    def mostrar_inventario(self):
        """Muestra todos los productos disponibles en el inventario."""
        print("\n" + "=" * 100)
        print("                Inventario de Productos")
        print("=" * 100)
        print(f"{'Nombre':<30} | {'Categoría':<20} | {'Precio':<10} | {'Cantidad':<10}")
        print("-" * 100)

        for producto in self.productos:
            print(producto)

        print("=" * 100)

    
    def agregar_producto(self):
        """Agrega un nuevo producto al inventario."""
        print("\n" + "=" * 100)
        print("                Agregar Producto")
        print("=" * 100)

        nombre = self.obtener_input_no_vacio("Nombre (puede incluir espacios): ")
        for producto in self.productos:
            if producto.get_nombre().lower() == nombre.lower():
                print(f"|| El producto '{nombre}' ya existe en el inventario.")
                self.modo_espera()
                return  # Volver al menú sin agregar el producto

        categoria = self.obtener_input_no_vacio("Categoría (puede incluir espacios): ")
        precio = self.obtener_precio_valido("Precio: ")
        cantidad = self.obtener_cantidad_valida("Cantidad: ")

        producto = Producto(nombre, categoria, precio, cantidad)
        self.productos.append(producto) # Añadir el nuevo producto a la lista
        print(f"|| El producto '{nombre}' ha sido agregado con éxito al inventario.")
        self.modo_espera()

    
    def eliminar_producto(self):
        """Elimina un producto del inventario."""
        self.mostrar_inventario() # Mostrar el inventario antes de eliminar
        print("\n" + "=" * 100)
        print("                Eliminar Producto")
        print("=" * 100)

        producto_eliminado = input("Elija el nombre del producto que desea eliminar: ").strip()
        for producto in self.productos:
            if producto.get_nombre().lower() == producto_eliminado.lower():
                self.productos.remove(producto) # Eliminar el producto de la lista
                print(f"|| El producto '{producto_eliminado}' ha sido eliminado con éxito.")
                self.modo_espera()
                return
        
        print(f"|| El producto '{producto_eliminado}' no existe en el inventario.")
        self.modo_espera()

    # Función para buscar productos en el inventario
    def buscar_producto(self):
        """Busca productos en el inventario por nombre."""
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
            print("\n || Productos encontrados:")
            print("=" * 100)
            for producto in encontrados:
                print(producto)
            print("=" * 100)
        else:
            print(f"|| El producto '{buscar_producto}' no existe en el inventario.")

        self.modo_espera()

    def actualizar_producto(self):
        """Actualiza los datos de un producto en el inventario."""
        print("\n" + "=" * 100)
        print("                Actualizar Producto")
        print("=" * 100)
        print("En caso de no querer modificar ese dato, simplemente dejarlo en blanco saltando la casilla con Enter.")
        producto_actualizar = self.obtener_input_no_vacio("Nombre del producto a actualizar (puede incluir espacios): ").strip()

        for producto in self.productos:
            if producto.get_nombre().lower() == producto_actualizar.lower():

                #  Pedir nuevos valores para actualizar, con opciones para dejar en blanco
                nuevo_nombre = self.obtener_valor_actualizado("Nuevo nombre", producto.get_nombre())
                nueva_categoria = self.obtener_valor_actualizado("Nueva categoría", producto.get_categoria())
                precio_nuevo = self.obtener_precio_valido(f"Nuevo precio (actual: {producto.get_precio()}): ", producto.get_precio())
                cantidad_nueva = self.obtener_cantidad_valida(f"Nueva cantidad (actual: {producto.get_cantidad()}): ", producto.get_cantidad())
                

                #Confirmación de la actualización del producto
                print("=" * 100)
                print ("| Datos del producto actualizados:")
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
                    self.modo_espera()
                    return
                else:
                    print("| !! La actualización ha sido cancelada.")
                    self.modo_espera()
                    return
        
        print(f"|| El producto '{producto_actualizar}' no existe en el inventario o no lo ha escrito correctamente.")
        self.modo_espera()
    
    def obtener_valor_actualizado (self,mensaje,valor_actual):
        """Solicita al usuario un nuevo valor para un atributo y permite dejarlo en blanco para conservar el valor actual."""
        nuevo_valor = input(f"{mensaje} (actual: {valor_actual}): ").strip()
        return nuevo_valor if nuevo_valor else valor_actual

    def obtener_input_no_vacio(self, mensaje):
        """Solicita al usuario un input y verifica que no esté vacío."""
        while True:
            entrada = input(mensaje).strip()
            if entrada:
                return entrada
            print("| !! La entrada no puede estar vacía.")


    def obtener_precio_valido(self, mensaje, precio_actual=None):
        """Solicita un precio válido al usuario."""
        while True:
            precio = input(mensaje)
            if not precio and precio_actual is not None:  # Si no se ingresa nada, usar el precio actual
                return precio_actual
            try:
                precio = float(precio)
                if precio <= 0:
                    print("| !! El precio no debe ser cero o menor a ese valor.")
                else:
                    return precio
            except ValueError:
                print("| !! El precio debe ser un número.")
            

    def obtener_cantidad_valida(self, mensaje, cantidad_actual=None):
        """Solicita una cantidad válida al usuario."""
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
    

    
    def mostrar_menu(self):
        """Muestra el menú principal y ejecuta las opciones seleccionadas."""
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
        """Mantiene el programa encendido en tiempo de ejecución."""
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
                        self.modo_espera()
                else:
                    print("| !! Opción no válida, elija un número del 1 al 6.")
            else:
                print("| !! Opción no válida, debe ser un número.")

        # Guardar el inventario en el archivo al salir
        self.guardar_inventario_en_archivo()


# Ejecución del programa
if __name__ == "__main__":
    inventario = Inventario()  # Crear una instancia de la clase Inventario
    inventario.run() # Iniciar el programa
