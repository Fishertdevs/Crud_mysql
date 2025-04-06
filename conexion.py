import mysql.connector
from mysql.connector import Error

class GestionProductos:

    def __init__(self):
        """Inicializa la conexión con la base de datos."""
        self.conexion = None
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,  # Cambia este puerto si tu servidor MySQL usa otro
                database='inventario_db',
                user='root',  # Cambia esto si usas otro usuario
                password='admin'  # Cambia esto si usas otra contraseña
            )
            if self.conexion.is_connected():
                print("Conexión establecida con éxito a la base de datos.")
        except Error as err:
            print(f"No se pudo conectar a la base de datos: {err}")

    def agregar_producto(self, codigo, nombre, modelo, precio, cantidad):
        """Inserta un nuevo producto en la tabla 'productos'."""
        if not self.conexion or not self.conexion.is_connected():
            print("No hay conexión a la base de datos.")
            return
        try:
            with self.conexion.cursor() as cursor:
                consulta = '''
                INSERT INTO productos (codigo, nombre, modelo, precio, cantidad) 
                VALUES (%s, %s, %s, %s, %s)
                '''
                cursor.execute(consulta, (codigo, nombre, modelo, precio, cantidad))
                self.conexion.commit()
                print("Producto añadido correctamente.")
        except Error as err:
            print(f"Error al agregar el producto: {err}")

    def listar_productos(self):
        """Obtiene y devuelve todos los productos de la tabla."""
        if not self.conexion or not self.conexion.is_connected():
            print("No hay conexión a la base de datos.")
            return []
        try:
            with self.conexion.cursor() as cursor:
                consulta = "SELECT * FROM productos"
                cursor.execute(consulta)
                productos = cursor.fetchall()
                return productos
        except Error as err:
            print(f"Error al obtener los productos: {err}")
            return []

    def buscar_producto(self, nombre_producto):
        """Busca un producto en la tabla por su nombre."""
        if not self.conexion or not self.conexion.is_connected():
            print("No hay conexión a la base de datos.")
            return []
        try:
            with self.conexion.cursor() as cursor:
                consulta = "SELECT * FROM productos WHERE nombre = %s"
                cursor.execute(consulta, (nombre_producto,))
                resultado = cursor.fetchall()
                return resultado
        except Error as err:
            print(f"Error al buscar el producto: {err}")
            return []

    def eliminar_producto(self, nombre_producto):
        """Elimina un producto de la tabla por su nombre."""
        if not self.conexion or not self.conexion.is_connected():
            print("No hay conexión a la base de datos.")
            return
        try:
            with self.conexion.cursor() as cursor:
                consulta = "DELETE FROM productos WHERE nombre = %s"
                cursor.execute(consulta, (nombre_producto,))
                self.conexion.commit()
                print("Producto eliminado exitosamente.")
        except Error as err:
            print(f"Error al eliminar el producto: {err}")