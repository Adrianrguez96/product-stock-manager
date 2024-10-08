import pytest
from main import Producto, Inventario  # Asegúrate de que el nombre del archivo principal sea 'inventario.py'

# Prueba de la clase Producto
def test_producto():
    # Crear un producto
    p = Producto("Tinta", "Impresoras", 10.5, 50)
    
    # Verificar los valores iniciales
    assert p.get_nombre() == "Tinta"
    assert p.get_categoria() == "Impresoras"
    assert p.get_precio() == 10.5
    assert p.get_cantidad() == 50

    # Cambiar valores usando setters
    p.set_precio(12.0)
    p.set_cantidad(40)
    assert p.get_precio() == 12.0
    assert p.get_cantidad() == 40

    # Probar validaciones en los setters
    p.set_precio(-5)
    assert p.get_precio() == 12.0  # Debería permanecer igual

    p.set_cantidad(-1)
    assert p.get_cantidad() == 40  # Debería permanecer igual

# Prueba de la clase Inventario
def test_inventario():
    inv = Inventario()

    # Asegurarse de que el inventario esté inicialmente vacío
    assert len(inv.productos) == 0

    # Agregar productos
    inv.productos.append(Producto("Tinta", "Impresoras", 10.5, 50))
    inv.productos.append(Producto("Papel", "Escritura", 5.0, 100))
    
    assert len(inv.productos) == 2  # Debería haber 2 productos

    # Verificar que se puedan buscar productos
    inv.buscar_producto()  # Esto debería ejecutarse sin errores

    # Eliminar un producto
    inv.eliminar_producto()  # Esto debería funcionar sin errores
    assert len(inv.productos) == 1  # Debería quedar solo 1 producto

    # Probar la función de búsqueda
    inv.buscar_producto()  # Esto debería ejecutarse sin errores

    # Probar la funcionalidad de guardar (solo verifica que no haya errores)
    inv.guardar_inventario_en_archivo()

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main()
