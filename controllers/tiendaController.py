class TiendaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            producto = self.vista.menu_crear_producto()
            self.modelo.crear_producto(producto)
        if opcion == 2:
            self.modelo.leer_productos()
        if opcion == 3:
            self.modelo.actualizar_producto(
                self.vista.solicitar_dato("ID del producto: "),
                self.vista.solicitar_dato("Nombre del producto: "),
                self.vista.solicitar_dato("Descripción del producto: "),
                self.vista.solicitar_dato("Precio del producto: ")
            )
        if opcion == 4:
            self.modelo.borrar_producto(self.vista.solicitar_dato("ID del producto: "))
