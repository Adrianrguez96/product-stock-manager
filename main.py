import os  # Librería de funciones de la consola de comandos

# Clase para los productos
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    # Getters de la clase Producto
    def get_nombre(self):
        return self.nombre
    
    def get_categoria(self):
        return self.categoria
    
    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad
    
    # Setters de la clase Producto
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_categoria(self, categoria):
        self.categoria = categoria
    
    def set_precio(self, precio):
        if precio <= 0:
            print("| !! El precio no puede ser negativo.")
            return
        self.precio = precio

    def set_cantidad(self, cantidad):
        if cantidad <= 0:
            print("| !! La cantidad no puede ser negativa.")
            return
        self.cantidad = cantidad


# Clase para el inventario
class Inventario:

    def __init__(self):
        self.productos = []  # Lista de productos
        self.cargar_productos()

    # Función para cargar los productos al inventario desde un archivo
    def cargar_productos(self):
        try:
            with open('inventario.txt', 'r') as archivo:
                for linea in archivo:
                    nombre, categoria, precio, cantidad = linea.strip().split(',')
                    producto = Producto(nombre, categoria, float(precio), int(cantidad))
                    self.productos.append(producto)  # Agregar productos a la lista
            print("Inventario cargado correctamente.")
        
        except FileNotFoundError:
            print("Archivo inventario.txt no encontrado. Se creará uno nuevo.")
            open('inventario.txt', 'w').close()
    
    # Función para borrar la pantalla dependiendo del sistema operativo
    def borrar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #Función para mostrar todo el inventario de productos del sistema
    def mostrar_inventario(self):
        print("\n" + "="*100)
        print("                Inventario de Productos")
        print("="*100)
        print(f"{'Nombre':<30} | {'Categoría':<20} | {'Precio':<10} | {'Cantidad':<10}")
        print("-"*100)
        
        for producto in self.productos:
            print(f"{producto.get_nombre():<30} | {producto.get_categoria():<20} | "
                  f"{producto.get_precio():<10.2f} | {producto.get_cantidad():<10}")
            
            print("="*100)
        
        # Esperar hasta que el usuario presione Enter
        print("\nPresione Enter para volver al menú...")
        input()
        self.borrar_pantalla()

    # Menú del programa con diferentes opciones
    def mostrar_menu(self):
        print("\n" + "="*100)
        print("      📦  Bienvenido al Inventario de Productos  📦")
        print("="*100)
        print("1  | Agregar producto")
        print("2  | Eliminar producto")
        print("3  | Buscar producto")
        print("4  | Actualizar producto")
        print("5  | Mostrar inventario")
        print("6  | Salir")
        print("="*100)
        print("  Elige una opción del 1 al 6: ")
    
    def run(self):
        self.menu_opcion = -1
        
        # Bucle del menú de opciones del programa
        while self.menu_opcion != 6:
            self.mostrar_menu()
            opcion = input("Elija una opción (1-6): ")
            self.borrar_pantalla()

            if opcion.isdigit():
                self.menu_opcion = int(opcion)

                if 1 <= self.menu_opcion <= 6:
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


# Hilo principal del programa y su carga
if __name__ == "__main__":
    inventario = Inventario()
    inventario.run()
