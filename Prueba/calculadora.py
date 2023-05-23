class Producto:
    def __init__(self, nombre, tipo, cantidad_actual, cantidad_minima, precio_base):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad_actual = cantidad_actual
        self.cantidad_minima = cantidad_minima
        self.precio_base = precio_base
    def calcular_precio_final(self):
        impuestos = 0
        if self.tipo == "Papelería":
            impuestos = 0.16
        elif self.tipo == "Supermercado":
            impuestos = 0.04
        elif self.tipo == "Droguería":
            impuestos = 0.12

        precio_final = self.precio_base * (1 + impuestos)
        return precio_final

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.dinero_en_caja = 0
        self.estadisticas_ventas = {}

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                print("Ya existe un producto con ese nombre.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def mostrar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre} - Tipo: {producto.tipo} - Cantidad: {producto.cantidad_actual} - Precio Base: {producto.precio_base}")

    def vender_producto(self, nombre_producto, cantidad):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto_encontrado = producto
                break

        if producto_encontrado:
            if cantidad <= producto_encontrado.cantidad_actual:
                precio_final = producto_encontrado.calcular_precio_final()
                total_venta = precio_final * cantidad
                self.dinero_en_caja += total_venta

                producto_encontrado.cantidad_actual -= cantidad

                if producto_encontrado.nombre in self.estadisticas_ventas:
                    self.estadisticas_ventas[producto_encontrado.nombre] += cantidad
                else:
                    self.estadisticas_ventas[producto_encontrado.nombre] = cantidad

                print(f"Venta realizada: {cantidad} {nombre_producto} - Total: {total_venta}")
            else:
                print("No hay suficiente cantidad del producto en la tienda.")
        else:
            print("No se encontró el producto.")

    def abastecer_producto(self, nombre_producto, cantidad):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto_encontrado = producto
                break

        if producto_encontrado:
            producto_encontrado.cantidad_actual += cantidad
            print(f"Producto {nombre_producto} abastecido correctamente.")
        else:
            print("No se encontró el producto.")

    def cambiar_producto(self, nombre_producto, tipo, cantidad_minima, precio_base):
        producto_encontrado = None
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto_encontrado = producto
                break

        if producto_encontrado:
            producto_encontrado.tipo = tipo
            producto_encontrado.cantidad_minima = cantidad_minima
            producto_encontrado.precio_base = precio_base
            print(f"Producto {nombre_producto} actualizado correctamente.")
        else:
            print("No se encontró el producto.")

    def calcular_estadisticas_ventas(self):
        if not self.estadisticas_ventas:
            print("Aún no se han realizado ventas.")
            return

        producto_mas_vendido = max(self.estadisticas_ventas, key=self.estadisticas_ventas.get)
        producto_menos_vendido = min(self.estadisticas_ventas, key=self.estadisticas_ventas.get)
        total_dinero_ventas = sum([self.producto_por_nombre(nombre).calcular_precio_final() * cantidad for nombre, cantidad in self.estadisticas_ventas.items()])
        promedio_dinero_unidad_vendida = total_dinero_ventas / sum(self.estadisticas_ventas.values())

        print("Estadísticas de ventas:")
        print(f"Producto más vendido: {producto_mas_vendido}")
        print(f"Producto menos vendido: {producto_menos_vendido}")
        print(f"Cantidad total de dinero obtenido por las ventas de la tienda: {total_dinero_ventas}")
        print(f"Cantidad de dinero promedio obtenido por unidad de producto vendida: {promedio_dinero_unidad_vendida}")

    def producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None


# Crear una tienda
tienda = Tienda("Mi Tienda")

# Agregar productos a la tienda
producto1 = Producto("cuaderno", "Papelería", 100, 10, 10.0)
producto2 = Producto("Sal", "Supermercado", 50, 5, 20.0)
producto3 = Producto("Shampoo", "Droguería", 80, 8, 5.0)
producto4 = Producto("Aceite", "Supermercado", 20, 3, 2.75 )


tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)
tienda.agregar_producto(producto4)


# Mostrar los productos de la tienda
tienda.mostrar_productos()

# Realizar una venta
nombre_producto = "cuaderno"
cantidad = 3
tienda.vender_producto(nombre_producto, cantidad)

# Abastecer un producto
nombre_producto = "Shampoo"
cantidad = 7
tienda.abastecer_producto(nombre_producto, cantidad)

# Cambiar un producto
nombre_producto = "Sal"
tipo = "Supermercado"
cantidad_minima = 5
precio_base = 2.5
tienda.cambiar_producto(nombre_producto, tipo, cantidad_minima, precio_base)

# Calcular estadísticas de ventas
tienda.calcular_estadisticas_ventas()
