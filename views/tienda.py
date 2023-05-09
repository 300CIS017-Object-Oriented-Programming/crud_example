import models.producto as productoModel
import models.inventario as inventarioModel
import controllers.tiendaController as tiendaController
import streamlit as st

class Tienda:
    def __init__(self):
        self.inventario = inventarioModel.Inventario()
        self.controlador = tiendaController.TiendaController(self.inventario, self)

    def mostrar_menu(self):
        st.title("Bienvenido a la tienda")

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Crear producto")
            boton_crear_producto = col1.button("Acceder a esta opción", 1)
            col2.header("Listar productos")
            boton_listar_productos = col2.button("Acceder a esta opción", 2)

        with st.container():
            col1, col2 = st.columns(2)
            col1.header("Actualizar producto")
            boton_actualizar_producto = col1.button("Acceder a esta opción", 3)
            col2.header("Borrar producto")
            boton_borrar_producto = col2.button("Acceder a esta opción", 4)

        if boton_crear_producto:
            st.session_state["opcion"] = 1
        elif boton_listar_productos:
            st.session_state["opcion"] = 2
        elif boton_actualizar_producto:
            st.session_state["opcion"] = 3
        elif boton_borrar_producto:
            st.session_state["opcion"] = 4

        if "opcion" in st.session_state:
            self.controlador.ejecutar_opcion(st.session_state["opcion"])

    def listar_productos(self, productos):
        st.divider()
        with st.container():
            st.subheader("Listado de productos disponibles")
            if len(productos) == 0:
                st.error("No hay productos para mostrar")
            else:
                for producto in productos:
                    st.markdown(f'**:red[ID del producto: ]** {producto.id}')
                    st.markdown(f'**:red[Nombre del producto: ]** {producto.nombre}')
                    st.markdown(f'**:red[Descripción del producto: ]** {producto.descripcion}')
                    st.markdown(f'**:red[Precio del producto: ]** ${producto.precio}')

    def menu_crear_producto(self):
        st.divider()
        with st.container():
            st.subheader("Formulario para crear un nuevo producto")
            id = st.text_input("ID del producto:")
            nombre = st.text_input("Nombre del producto:")
            descripcion = st.text_input("Descripción del producto:")
            precio = st.slider("Precio del producto:", min_value = 1000, max_value = 50000, step = 100)
            boton_accion = st.button("Crear nuevo producto")

        if boton_accion:
            if not id.isnumeric():
                raise ValueError("El ID debe ser un valor numérico")

            nuevoProducto = productoModel.Producto(id, nombre, descripcion, precio)
            st.success("El producto fue creado correctamente")
            return nuevoProducto

    def menu_actualizar_producto(self, productos):
        st.divider()
        with st.container():
            st.subheader("Formulario para actualizar un producto existente")
            if len(productos) == 0:
                st.error("No hay productos para actualizar")
            else:
                opciones = []
                for producto in productos:
                    opciones.append(producto.id)
                id = st.selectbox("Producto a modificar:", opciones)
                nuevo_nombre = st.text_input("Nombre del producto:")
                nueva_descripcion = st.text_input("Descripción del producto:")
                nuevo_precio = st.slider("Precio del producto:", min_value = 1000, max_value = 50000, step = 100)
                boton_accion = st.button("Actualizar producto")

                if boton_accion:
                    self.inventario.actualizar_producto(id, nuevo_nombre, nueva_descripcion, nuevo_precio)
                    st.success("El producto fue actualizado correctamente")

    def menu_borrar_producto(self, productos):
        st.divider()
        with st.container():
            st.subheader("Formulario para elimiar un producto existente")
            if len(productos) == 0:
                st.error("No hay productos para eliminar")
            else:
                nombres = []
                opciones = {}
                for producto in productos:
                    nombres.append(producto.nombre)
                    opciones[producto.nombre] = producto.id
                nombre = st.selectbox("Producto a eliminar:", nombres)
                boton_accion = st.button("Borrar producto seleccionado")

                if boton_accion:
                    return opciones[nombre]

    def mostrar_mensaje_exitoso(self, mensaje):
        st.success(mensaje)

    def mostrar_mensaje_error(self, mensaje):
        st.error(mensaje)
