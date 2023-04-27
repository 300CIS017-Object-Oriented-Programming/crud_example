import models.producto as productoModel
import models.inventario as inventarioModel
import controllers.tiendaController as tiendaController

class Tienda:
    def mostrar_menu(self):
        print("- Bienvenido a la tienda -")
        inventario = inventarioModel.Inventario()
        controlador = tiendaController.TiendaController(inventario, self)

        while True:
            print("\nOpciones disponibles")
            print("1. Crear producto")
            print("2. Listar productos")
            print("3. Actualizar producto")
            print("4. Borrar producto")
            print("0. Salir")

            opcion = int(input("Por favor ingrese una opción: "))

            if opcion == 0:
                print("\n- Gracias por visitarnos -")
                break
            else:
                controlador.ejecutar_opcion(opcion)

    def menu_crear_producto(self):
        id = input("ID producto:")
        nombre = input("Nombre producto:")
        descripcion = input("Descripción producto:")
        precio = input("Precio producto:")

        nuevoProducto = productoModel.Producto(id, nombre, descripcion, precio)
        return nuevoProducto

    def solicitar_dato(self, mensaje):
        return input(mensaje)