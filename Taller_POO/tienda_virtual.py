# -----------------------------
# Tienda Virtual
# -----------------------------

class Cliente:
    def __init__(self, ID_cliente, nombre, telefono, email, direccion, fecha_nacimiento):
        self.ID_cliente = ID_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_informacion(self):
        print(f"Cliente [{self.ID_cliente}] - {self.nombre}")
        print(f"Teléfono: {self.telefono}, Email: {self.email}")
        print(f"Dirección: {self.direccion}, Fecha de nacimiento: {self.fecha_nacimiento}")

    def comprar(self, producto):
        print(f"{self.nombre} ha comprado el producto: {producto.nombre_producto} por ${producto.precio_unitario}")


class Vendedor:
    def __init__(self, ID_vendedor, ciudad, contacto, tipos_productos):
        self.ID_vendedor = ID_vendedor
        self.ciudad = ciudad
        self.contacto = contacto
        self.tipos_productos = tipos_productos

    def mostrar_informacion(self):
        print(f"Vendedor [{self.ID_vendedor}]")
        print(f"Ciudad: {self.ciudad}, Contacto: {self.contacto}")
        print(f"Tipos de productos: {self.tipos_productos}")

    def confirmar_pedido(self, cliente, producto):
        print(f"Pedido confirmado para {cliente.nombre}: {producto.nombre_producto}")

    def generar_factura(self, ID_factura, cliente, producto):
        total = producto.precio_unitario
        return Factura(ID_factura, cliente.ID_cliente, self.ID_vendedor, producto.ID_producto, total)


class Producto:
    def __init__(self, ID_producto, nombre_producto, precio_unitario):
        self.ID_producto = ID_producto
        self.nombre_producto = nombre_producto
        self.precio_unitario = precio_unitario

    def mostrar_informacion(self):
        print(f"Producto [{self.ID_producto}] - {self.nombre_producto}, Precio: ${self.precio_unitario}")


class Factura:
    def __init__(self, ID_factura, ID_cliente, ID_vendedor, ID_producto, precio_total):
        self.ID_factura = ID_factura
        self.ID_cliente = ID_cliente
        self.ID_vendedor = ID_vendedor
        self.ID_producto = ID_producto
        self.precio_total = precio_total

    def mostrar_informacion(self):
        print(f"Factura [{self.ID_factura}]")
        print(f"Cliente ID: {self.ID_cliente}, Vendedor ID: {self.ID_vendedor}, Producto ID: {self.ID_producto}")
        print(f"Precio total: ${self.precio_total}")


# -----------------------------
# Ejemplo de uso del programa
# -----------------------------
if __name__ == "__main__":
    # Crear objetos
    cliente1 = Cliente(1, "Ana Pérez", "3124567890", "ana@mail.com", "Calle 123", "1995-04-20")
    vendedor1 = Vendedor(101, "Bogotá", "3209876543", "Ropa, Zapatos")
    producto1 = Producto(501, "Camisa Blanca", 45000)

    # Cliente compra producto
    cliente1.mostrar_informacion()
    producto1.mostrar_informacion()
    cliente1.comprar(producto1)

    # Vendedor confirma y genera factura
    vendedor1.mostrar_informacion()
    vendedor1.confirmar_pedido(cliente1, producto1)
    factura1 = vendedor1.generar_factura(9001, cliente1, producto1)

    # Mostrar factura
    factura1.mostrar_informacion()