from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from conexion import GestionProductos  # Importa la clase correcta


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Paneles principales
        self.frame1 = Frame(master, bg='black')
        self.frame1.grid(columnspan=2, column=0, row=0)
        self.frame2 = Frame(master, bg='black')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master, bg='black')
        self.frame3.grid(rowspan=2, column=1, row=1)
        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)
        self.frame5 = Frame(master, bg='black')  # Pie de página
        self.frame5.grid(columnspan=2, column=0, row=3, pady=10)

        # Variables
        self.codigo = StringVar()
        self.nombre = StringVar()
        self.modelo = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        self.buscar = StringVar()

        # Instancia la clase correcta desde conexion.py
        self.base_datos = GestionProductos()
        self.create_widgets()

    def create_widgets(self):
        # Título principal
        Label(self.frame1, text='R E G I S T R O   D E   D A T O S', bg='black', fg='lime', font=('Orbitron', 15, 'bold')).grid(column=0, row=0)

        # Etiquetas y entradas para agregar datos
        Label(self.frame2, text='Agregar Nuevos Datos', fg='lime', bg='black', font=('Rockwell', 12, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame2, text='Código', fg='lime', bg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=1, pady=15)
        Label(self.frame2, text='Nombre', fg='lime', bg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=2, pady=15)
        Label(self.frame2, text='Modelo', fg='lime', bg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=3, pady=15)
        Label(self.frame2, text='Precio', fg='lime', bg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=4, pady=15)
        Label(self.frame2, text='Cantidad', fg='lime', bg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=5, pady=15)

        Entry(self.frame2, textvariable=self.codigo, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime').grid(column=1, row=1, padx=5)
        Entry(self.frame2, textvariable=self.nombre, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime').grid(column=1, row=2)
        Entry(self.frame2, textvariable=self.modelo, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime').grid(column=1, row=3)
        Entry(self.frame2, textvariable=self.precio, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime').grid(column=1, row=4)
        Entry(self.frame2, textvariable=self.cantidad, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime').grid(column=1, row=5)

        # Botones de control
        Label(self.frame4, text='Control', fg='lime', bg='black', font=('Rockwell', 12, 'bold')).grid(columnspan=3, column=0, row=0, pady=1, padx=4)
        Button(self.frame4, command=self.agregar_datos, text='REGISTRAR', font=('Arial', 10, 'bold'), bg='lime', fg='black').grid(column=0, row=1, pady=10, padx=4)
        Button(self.frame4, command=self.limpiar_datos, text='LIMPIAR', font=('Arial', 10, 'bold'), bg='lime', fg='black').grid(column=1, row=1, padx=10)
        Button(self.frame4, command=self.eliminar_fila, text='ELIMINAR', font=('Arial', 10, 'bold'), bg='lime', fg='black').grid(column=2, row=1, padx=4)
        Button(self.frame4, command=self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial', 8, 'bold'), bg='lime', fg='black').grid(columnspan=2, column=1, row=2)
        Entry(self.frame4, textvariable=self.buscar, font=('Arial', 12), bg='black', fg='lime', insertbackground='lime', width=10).grid(column=0, row=2, pady=1, padx=8)
        Button(self.frame4, command=self.mostrar_todo, text='MOSTRAR DATOS DE MYSQL', font=('Arial', 10, 'bold'), bg='lime', fg='black').grid(columnspan=3, column=0, row=3, pady=8)

        # Tabla para mostrar datos
        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130, anchor='center')
        self.tabla.column('Modelo', minwidth=100, width=120, anchor='center')
        self.tabla.column('Precio', minwidth=100, width=120, anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Código', anchor='center')
        self.tabla.heading('Nombre', text='Nombre', anchor='center')
        self.tabla.heading('Modelo', text='Modelo', anchor='center')
        self.tabla.heading('Precio', text='Precio', anchor='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor='center')

        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure(".", font=('Helvetica', 12, 'bold'), foreground='lime')
        estilo.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black', background='white')
        estilo.map('Treeview', background=[('selected', 'lime')], foreground=[('selected', 'black')])

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)

        # Pie de página
        Label(self.frame5, text="Desarrollado por Harry Fishert - GitHub", bg='black', fg='lime', font=('Arial', 10, 'italic')).grid(column=0, row=0)

    def agregar_datos(self):
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        modelo = self.modelo.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        datos = (nombre, modelo, precio, cantidad)
        if codigo and nombre and modelo and precio and cantidad != '':
            self.tabla.insert('', 0, text=codigo, values=datos)
            self.base_datos.agregar_producto(codigo, nombre, modelo, precio, cantidad)

    def limpiar_datos(self):
        self.codigo.set('')
        self.nombre.set('')
        self.modelo.set('')
        self.precio.set('')
        self.cantidad.set('')

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_buscado = self.base_datos.buscar_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        for i, dato in enumerate(nombre_buscado):
            self.tabla.insert('', i, text=dato[0], values=dato[1:])

    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.listar_productos()
        for i, dato in enumerate(registro):
            self.tabla.insert('', i, text=dato[0], values=dato[1:])

    def eliminar_fila(self):
        fila = self.tabla.selection()
        if fila:
            self.tabla.delete(fila)
            nombre = self.nombre.get()
            self.base_datos.eliminar_producto(nombre)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre.set(data['values'][0])


def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='black')
    ventana.geometry('900x550')
    ventana.resizable(0, 0)
    app = Registro(ventana)
    app.mainloop()


if __name__ == "__main__":
    main()