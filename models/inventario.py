class Inventario:
    def __init__(self):
        self.productos = []

    def crear_producto(self, producto):
        self.productos.append(producto)

    def leer_productos(self):
        print("Listado de productos:")
        for producto in self.productos:
            producto.mostrar()

    def actualizar_producto(self, id, nombre = None, descripcion = None, precio = None):
        for producto in self.productos:
            if producto.id == id:
                if nombre:
                    producto.nombre = nombre
                if descripcion:
                    producto.descripcion = descripcion
                if precio:
                    producto.precio = precio

    def borrar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                self.productos.pop(i)
