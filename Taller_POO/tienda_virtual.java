// Clase Cliente
class Cliente {
    int ID_cliente;
    String nombre;
    String telefono;
    String email;
    String direccion;
    String fecha_nacimiento;

    public Cliente(int ID_cliente, String nombre, String telefono, String email, String direccion, String fecha_nacimiento) {
        this.ID_cliente = ID_cliente;
        this.nombre = nombre;
        this.telefono = telefono;
        this.email = email;
        this.direccion = direccion;
        this.fecha_nacimiento = fecha_nacimiento;
    }

    public void mostrarInformacion() {
        System.out.println("Cliente: " + nombre + " (ID: " + ID_cliente + ")");
        System.out.println("Teléfono: " + telefono);
        System.out.println("Email: " + email);
        System.out.println("Dirección: " + direccion);
        System.out.println("Fecha de nacimiento: " + fecha_nacimiento);
    }

    public void comprar() {
        System.out.println(nombre + " ha realizado una compra.");
    }
}

// Clase Vendedor
class Vendedor {
    int ID_vendedor;
    String ciudad;
    String contacto;
    String tipos_productos;

    public Vendedor(int ID_vendedor, String ciudad, String contacto, String tipos_productos) {
        this.ID_vendedor = ID_vendedor;
        this.ciudad = ciudad;
        this.contacto = contacto;
        this.tipos_productos = tipos_productos;
    }

    public void mostrarInformacion() {
        System.out.println("Vendedor (ID: " + ID_vendedor + ")");
        System.out.println("Ciudad: " + ciudad);
        System.out.println("Contacto: " + contacto);
        System.out.println("Tipos de productos: " + tipos_productos);
    }

    public void confirmarPedido() {
        System.out.println("El vendedor ha confirmado el pedido.");
    }

    public void generarFactura() {
        System.out.println("El vendedor ha generado la factura.");
    }
}

// Clase Producto
class Producto {
    int ID_producto;
    String nombre_producto;
    double precio_unitario;

    public Producto(int ID_producto, String nombre_producto, double precio_unitario) {
        this.ID_producto = ID_producto;
        this.nombre_producto = nombre_producto;
        this.precio_unitario = precio_unitario;
    }

    public void mostrarInformacion() {
        System.out.println("Producto: " + nombre_producto + " (ID: " + ID_producto + ")");
        System.out.println("Precio unitario: $" + precio_unitario);
    }
}

// Clase Factura
class Factura {
    int ID_factura;
    int ID_cliente;
    int ID_vendedor;
    int ID_producto;
    double precio_total;

    public Factura(int ID_factura, int ID_cliente, int ID_vendedor, int ID_producto, double precio_total) {
        this.ID_factura = ID_factura;
        this.ID_cliente = ID_cliente;
        this.ID_vendedor = ID_vendedor;
        this.ID_producto = ID_producto;
        this.precio_total = precio_total;
    }

    public void mostrarInformacion() {
        System.out.println("Factura ID: " + ID_factura);
        System.out.println("Cliente ID: " + ID_cliente);
        System.out.println("Vendedor ID: " + ID_vendedor);
        System.out.println("Producto ID: " + ID_producto);
        System.out.println("Precio total: $" + precio_total);
    }
}

// Clase Principal
public class TiendaVirtual {
    public static void main(String[] args) {
        // Crear un cliente
        Cliente cliente1 = new Cliente(1, "María Pérez", "312345678", "maria@gmail.com", "Calle 123", "15/05/1995");
        cliente1.mostrarInformacion();
        cliente1.comprar();

        System.out.println("-------------------------");

        // Crear un vendedor
        Vendedor vendedor1 = new Vendedor(101, "Bogotá", "321987654", "Electrodomésticos");
        vendedor1.mostrarInformacion();
        vendedor1.confirmarPedido();
        vendedor1.generarFactura();

        System.out.println("-------------------------");

        // Crear un producto
        Producto producto1 = new Producto(501, "Televisor", 1500.00);
        producto1.mostrarInformacion();

        System.out.println("-------------------------");

        // Crear una factura
        Factura factura1 = new Factura(1001, cliente1.ID_cliente, vendedor1.ID_vendedor, producto1.ID_producto, producto1.precio_unitario);
        factura1.mostrarInformacion();
    }
}