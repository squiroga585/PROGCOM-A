class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Factura:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items)

    def mostrar(self):
        print("Factura del Supermercado")
        print("-" * 30)
        for producto, cantidad in self.items:
            print(f"{producto.nombre} x{cantidad} - ${producto.precio * cantidad:.2f}")
        print("-" * 30)
        print(f"Total: ${self.total():.2f}")

class CajeroSupermercado:
    def __init__(self):
        self.productos = [
            Producto("Manzanas", 1.50),
            Producto("Carne", 5.00),
            Producto("Lechuga", 1.00),
            Producto("Peras", 1.80),
            Producto("Dulces", 0.50),
            Producto("Leche", 2.00),
            Producto("Huevos", 3.00),
            Producto("Patacon", 1.20),
            Producto("Banana", 1.30),
            Producto("Coco", 2.50)
        ]

    def mostrar_productos(self):
        print("Productos disponibles:")
        for idx, producto in enumerate(self.productos, 1):
            print(f"{idx}. {producto.nombre} - ${producto.precio:.2f}")

    def iniciar(self):
        factura = Factura()
        while True:
            self.mostrar_productos()
            opcion = input("Seleccione el número del producto (o 'fin' para terminar): ")
            if opcion.lower() == 'fin':
                break
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > len(self.productos):
                print("Opción inválida. Intente de nuevo.")
                continue
            cantidad = input(f"Ingrese la cantidad de {self.productos[int(opcion)-1].nombre}: ")
            if not cantidad.isdigit() or int(cantidad) < 1:
                print("Cantidad inválida. Intente de nuevo.")
                continue
            factura.agregar_producto(self.productos[int(opcion)-1], int(cantidad))
        factura.mostrar()

if __name__ == "__main__":
    cajero = CajeroSupermercado()
    cajero.iniciar()