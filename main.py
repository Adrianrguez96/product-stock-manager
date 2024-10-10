import os  # Librería de funciones de la consola de comandos

# Clase para los productos
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        """
        Representa un producto con nombre, categoría, precio y cantidad.
        
        Atributos:
            _nombre (str): El nombre del producto.
            _categoria (str): La categoría a la que pertenece el producto.
            _precio (float): El precio del producto, debe ser mayor que 0.
            _cantidad (int): La cantidad disponible del producto, debe ser mayor o igual a 0.
        """

        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
    
    def __str__ (self):
        """
        Retorna una representación en forma de cadena del producto, formateada en columnas.
        """

        return f"{self._nombre:<30} | {self._categoria:<20} | {self._precio:<10.2f} | {self._cantidad:<10}"

    # Getters para acceder a los atributos privados
    def get_nombre(self):
        """
        Retorna el nombre del producto.
        """

        return self._nombre

    def get_categoria(self):
        """
        Retorna la categoria del producto.
        """

        return self._categoria

    def get_precio(self):
        """
        Retorna el precio del producto.
        """

        return self._precio

    def get_cantidad(self):
        """
        Retorna la cantidad del producto.
        """

        return self._cantidad

    # Setters para modificar los atributos, con validaciones
    def set_nombre(self, nombre):
        """
        Establece el nombre del producto.
        """

        self._nombre = nombre

    def set_categoria(self, categoria):
        """
        Establece el nombre de la categoria.
        """

        self._categoria = categoria

    def set_precio(self, precio):
        """
        Establece el precio del producto, validando que sea mayor que 0.
        """

        if precio <= 0:
            print("| !! El precio no puede ser negativo o cero.")
            return
        self._precio = precio

    def set_cantidad(self, cantidad):
        """
        Establece la cantidad del producto, validando que no sea negativa.
        """

        if cantidad < 0:
            print("| !! La cantidad no puede ser negativa.")
            return
        self._cantidad = cantidad


# Clase para el inventario
class Inventario:
    """
    Representa un inventario de productos, permite gestionar productos mediante varias acciones.

    Atributos:
        productos (list): Lista de productos en el inventario.
    """

    def __init__(self):
        """
        Inicializa el inventario y carga los productos desde un archivo.
        """

        self.productos = []  # Lista de productos
        self.cargar_productos() # Cargar productos desde el archivo al iniciar

    def cargar_productos(self):
        """
        Carga los productos desde el archivo 'inventario.txt'.

        Si el archivo no existe, lo crea. Si alguna línea no tiene el formato correcto, se ignora.
        """

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
        """
        Guarda el inventario actual en el archivo 'inventario.txt'.

        Sobrescribe el archivo cada vez que se llama a este método.
        """

        try:
            with open('inventario.txt', 'w') as archivo:
                for producto in self.productos:
                    # Guardar cada producto en una nueva línea en el formato especificado
                    archivo.write(f"{producto.get_nombre()},{producto.get_categoria()},{producto.get_precio()},{producto.get_cantidad()}\n")
                print("El archivo de inventario se ha actualizado correctamente.")
        except Exception as e:
            print(f"|| Error al guardar el archivo: {e}")

    def borrar_pantalla(self):
        """
        Limpia la pantalla de la consola, funciona en Windows ('cls') y Unix ('clear').
        """

        os.system('cls' if os.name == 'nt' else 'clear')
    
    def modo_espera(self):
        """
        Detiene la ejecución del programa hasta que el usuario presione Enter.

        Útil para hacer una pausa antes de regresar al menú principal.
        """

        print("\nPresione Enter para volver al menú...")
        input()
        self.borrar_pantalla()

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario, organizados en columnas.

        La salida incluye el nombre, categoría, precio y cantidad de cada producto.
        """
                
        print("\n" + "=" * 100)
        print("Inventario de Productos".center(100))
        print("=" * 100)
        print(f"{'Nombre':<30} | {'Categoría':<20} | {'Precio':<10} | {'Cantidad':<10}")
        print("-" * 100)
        
        print("\n".join(str(producto) for producto in self.productos))

        print("=" * 100)

    
    def agregar_producto(self):
        """
        Permite al usuario agregar un nuevo producto al inventario.

        Se valida que el producto no exista previamente y que los valores ingresados sean válidos.
        """

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
        precio = self.obtener_input_valido("Precio: ", "float")
        cantidad = self.obtener_input_valido("Cantidad: ", "int")

        producto = Producto(nombre, categoria, precio, cantidad)
        self.productos.append(producto) # Añadir el nuevo producto a la lista
        print(f"|| El producto '{nombre}' ha sido agregado con éxito al inventario.")
        self.modo_espera()

    
    def eliminar_producto(self):
        """
        Permite al usuario eliminar un producto del inventario.

        Si el producto no existe, se notifica al usuario.
        """

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
        """
        Busca un producto en el inventario por nombre.

        La búsqueda no es sensible a mayúsculas/minúsculas y permite buscar por palabras clave parciales.
        """
                
        buscar_producto = input("Buscar producto: ").strip()

        # Separar las palabras de búsqueda para realizar una búsqueda más flexible
        palabras_busqueda = [palabra.lower() for palabra in buscar_producto.split()]

        # Se crea una lista de compresión para realizar la busqueda eficientemente
        encontrados = [producto for producto in self.productos if all(palabra in producto.get_nombre().lower() for palabra in palabras_busqueda)]

        
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
        """
        Actualiza los datos de un producto existente en el inventario.

        Permite modificar el nombre, categoría, precio y cantidad. Los valores no modificados
        pueden dejarse en blanco.
        """
                
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
                precio_nuevo = self.obtener_input_valido(f"Nuevo precio (actual: {producto.get_precio()}): ", "float", producto.get_precio())
                cantidad_nueva = self.obtener_input_valido(f"Nueva cantidad (actual: {producto.get_cantidad()}): ", "int", producto.get_cantidad())
                

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
        """
        Solicita al usuario un nuevo valor para un atributo y permite dejarlo en blanco para conservar el valor actual.

        Parámetros:
            mensaje (str): El mensaje a mostrar al usuario.
            valor_actual (opcional): El valor actual a usar si no se ingresa un nuevo valor.
        
        Retorna:
            str: El valor ingresado por el usuario.
        """

        nuevo_valor = input(f"{mensaje} (actual: {valor_actual}): ").strip()
        return nuevo_valor if nuevo_valor else valor_actual

    def obtener_input_no_vacio(self, mensaje):
        """
        Solicita al usuario un input y verifica que no esté vacío.

        Parámetros:
            mensaje (str): El mensaje a mostrar al usuario.
        
        Retorna:
            str: El valor ingresado por el usuario.
        """

        while True:
            entrada = input(mensaje).strip()
            if entrada:
                return entrada
            print("| !! La entrada no puede estar vacía.")


    def obtener_input_valido(self, mensaje, tipo, valor_actual=None):
        """
        Solicita al usuario un valor numérico válido, y permite dejar en blanco para mantener el valor actual.

        Parámetros:
            mensaje (str): El mensaje a mostrar al usuario.
            tipo (str): Tipo de dato esperado ('float' o 'int').
            valor_actual (opcional): El valor actual a usar si no se ingresa un nuevo valor.
        
        Retorna:
            float o int: El valor ingresado por el usuario.
        """
        
        while True:
            valor = input(mensaje)

            if not valor and valor_actual is not None:  # Si no se ingresa nada, usar el valor actual
                return valor_actual

            try:
                if tipo == 'float':
                    valor = float(valor)
                    if valor <= 0: 
                        print("| !! El valor no debe ser cero o negativo.") 
                    else:
                        return valor
                    
                elif tipo == 'int':
                    valor = int(valor)
                    if valor < 0:
                        print("| !! El valor no puede ser negativo.")
                    else:
                        return valor
                    
            except ValueError:
                print("| !! El valor debe ser un número.")

    def mostrar_menu(self):
        """
        Muestra el menú principal con las opciones disponibles para gestionar el inventario.
        """

        print("\n" + "=" * 100)
        print("Bienvenido al Inventario de Productos".center(100))
        print("=" * 100)
        print("1  | Agregar producto")
        print("2  | Eliminar producto")
        print("3  | Buscar producto")
        print("4  | Actualizar producto")
        print("5  | Mostrar inventario")
        print("6  | Salir")
        print("=" * 100)

    def run(self):
        """
        Mantiene el programa en ejecución, mostrando el menú y gestionando las opciones seleccionadas.

        Permite al usuario realizar acciones como agregar, eliminar, buscar, actualizar, y mostrar productos.
        """

        self.menu_opcion = -1

        #Definir las acciones del menu en el diccionario
        acciones = {
            1: self.agregar_producto,
            2: self.eliminar_producto,
            3: self.buscar_producto,
            4: self.actualizar_producto,
            5: lambda: (self.mostrar_inventario(), self.modo_espera()),
            6: lambda: print("Saliendo del programa...")
        }
        
        while self.menu_opcion != 6:
            self.mostrar_menu() # Mostrar menú de opciones
            opcion = input("Elija una opción (1-6): ")
            self.borrar_pantalla()

            if opcion.isdigit():
                self.menu_opcion = int(opcion)
                if 1 <= self.menu_opcion <= len(acciones):
                    acciones[self.menu_opcion]()

        # Guardar el inventario en el archivo al salir
        self.guardar_inventario_en_archivo()


# Ejecución del programa
if __name__ == "__main__":
    inventario = Inventario()  # Crear una instancia de la clase Inventario
    inventario.run() # Iniciar el programa
