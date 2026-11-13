import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
from datetime import datetime

# Microtaller 6 - Control de ventas
# Responsable: Nelson Julián Martínez Bedoya
# No requiere pandas, matplotlib ni openpyxl.

VENTAS = [
    ('2026-11-01','Portátil','Tecnología','Bogotá','Carlos',2,2800000),
    ('2026-11-01','Mouse inalámbrico','Accesorios','Medellín','Laura',8,85000),
    ('2026-11-02','Teclado mecánico','Accesorios','Cali','Andrés',4,210000),
    ('2026-11-02','Monitor 24 pulgadas','Tecnología','Bogotá','Carlos',3,780000),
    ('2026-11-03','Disco SSD 1 TB','Almacenamiento','Barranquilla','Andrés',5,390000),
    ('2026-11-03','Portátil','Tecnología','Medellín','Laura',1,2800000),
    ('2026-11-04','Memoria USB 128 GB','Almacenamiento','Cali','Andrés',10,55000),
    ('2026-11-04','Audífonos','Accesorios','Bogotá','Carlos',6,145000),
    ('2026-11-05','Monitor 24 pulgadas','Tecnología','Medellín','Laura',2,780000),
    ('2026-11-05','Webcam HD','Accesorios','Bogotá','Carlos',5,180000),
    ('2026-11-06','Portátil','Tecnología','Cali','Andrés',1,2800000),
    ('2026-11-06','Mouse inalámbrico','Accesorios','Barranquilla','Laura',12,85000),
    ('2026-11-07','Disco SSD 1 TB','Almacenamiento','Bogotá','Carlos',3,390000),
    ('2026-11-07','Teclado mecánico','Accesorios','Medellín','Andrés',7,210000),
    ('2026-11-08','Monitor 24 pulgadas','Tecnología','Cali','Laura',2,780000),
    ('2026-11-08','Memoria USB 128 GB','Almacenamiento','Bogotá','Carlos',15,55000),
    ('2026-11-09','Audífonos','Accesorios','Medellín','Andrés',9,145000),
    ('2026-11-09','Webcam HD','Accesorios','Barranquilla','Laura',4,180000),
    ('2026-11-10','Portátil','Tecnología','Bogotá','Carlos',1,2800000),
    ('2026-11-10','Disco SSD 1 TB','Almacenamiento','Cali','Andrés',6,390000),
]

COLORES = {
    'fondo': '#F4F7FB', 'azul': '#1F4E78', 'azul2': '#2F75B5',
    'verde': '#5B9BD5', 'naranja': '#ED7D31', 'gris': '#5B6573',
    'blanco': '#FFFFFF', 'borde': '#D4DCE5'
}

def moneda(valor):
    return '$' + f'{valor:,.0f}'.replace(',', '.')

def calcular(ventas):
    total = sum(v[5] * v[6] for v in ventas)
    unidades = sum(v[5] for v in ventas)
    por_dia = defaultdict(int)
    por_producto = defaultdict(int)
    por_categoria = defaultdict(int)
    for fecha, producto, categoria, ciudad, vendedor, cantidad, precio in ventas:
        valor = cantidad * precio
        por_dia[fecha] += valor
        por_producto[producto] += valor
        por_categoria[categoria] += valor
    return total, unidades, por_dia, por_producto, por_categoria

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Control de ventas - Dashboard')
        self.geometry('1200x780')
        self.minsize(1000, 680)
        self.configure(bg=COLORES['fondo'])
        self.ventas = list(VENTAS)
        self.crear_estilos()
        self.crear_interfaz()
        self.actualizar_dashboard()

    def crear_estilos(self):
        estilo = ttk.Style(self)
        try:
            estilo.theme_use('clam')
        except tk.TclError:
            pass
        estilo.configure('Titulo.TLabel', background=COLORES['azul'], foreground='white', font=('Arial', 18, 'bold'))
        estilo.configure('Subtitulo.TLabel', background=COLORES['azul'], foreground='#DDEBF7', font=('Arial', 10))
        estilo.configure('Card.TFrame', background='white', relief='solid', borderwidth=1)
        estilo.configure('CardTitle.TLabel', background='white', foreground=COLORES['gris'], font=('Arial', 10, 'bold'))
        estilo.configure('CardValue.TLabel', background='white', foreground=COLORES['azul'], font=('Arial', 17, 'bold'))
        estilo.configure('TButton', font=('Arial', 10, 'bold'), padding=7)
        estilo.configure('Treeview', font=('Arial', 9), rowheight=25)
        estilo.configure('Treeview.Heading', font=('Arial', 9, 'bold'))

    def crear_interfaz(self):
        encabezado = tk.Frame(self, bg=COLORES['azul'], height=82)
        encabezado.pack(fill='x')
        encabezado.pack_propagate(False)
        tk.Label(encabezado, text='DASHBOARD DE CONTROL DE VENTAS', bg=COLORES['azul'], fg='white', font=('Arial', 19, 'bold')).pack(anchor='w', padx=25, pady=(13, 0))
        tk.Label(encabezado, text='Nelson Julián Martínez Bedoya  |  Microtaller 6  |  Periodo: 1 al 10 de noviembre de 2026', bg=COLORES['azul'], fg='#DDEBF7', font=('Arial', 10)).pack(anchor='w', padx=27, pady=(4, 0))

        barra = tk.Frame(self, bg=COLORES['fondo'])
        barra.pack(fill='x', padx=22, pady=(14, 7))
        ttk.Button(barra, text='Registrar nueva venta', command=self.abrir_formulario).pack(side='left')
        ttk.Button(barra, text='Actualizar dashboard', command=self.actualizar_dashboard).pack(side='left', padx=8)
        ttk.Button(barra, text='Ver registros', command=self.abrir_registros).pack(side='left')
        tk.Label(barra, text='Los datos se guardan durante esta sesión.', bg=COLORES['fondo'], fg=COLORES['gris'], font=('Arial', 9, 'italic')).pack(side='right')

        self.kpi_frame = tk.Frame(self, bg=COLORES['fondo'])
        self.kpi_frame.pack(fill='x', padx=22, pady=5)
        self.graficos = tk.Frame(self, bg=COLORES['fondo'])
        self.graficos.pack(fill='both', expand=True, padx=22, pady=(5, 20))

    def tarjeta(self, columna, titulo, valor, color):
        tarjeta = tk.Frame(self.kpi_frame, bg='white', highlightbackground=COLORES['borde'], highlightthickness=1)
        tarjeta.grid(row=0, column=columna, sticky='nsew', padx=5)
        self.kpi_frame.columnconfigure(columna, weight=1)
        tk.Label(tarjeta, text=titulo, bg='white', fg=COLORES['gris'], font=('Arial', 10, 'bold')).pack(anchor='w', padx=14, pady=(12, 1))
        tk.Label(tarjeta, text=valor, bg='white', fg=color, font=('Arial', 17, 'bold')).pack(anchor='w', padx=14, pady=(0, 12))

    def actualizar_dashboard(self):
        for widget in self.kpi_frame.winfo_children(): widget.destroy()
        for widget in self.graficos.winfo_children(): widget.destroy()
        total, unidades, por_dia, por_producto, por_categoria = calcular(self.ventas)
        self.tarjeta(0, 'VENTAS TOTALES', moneda(total), COLORES['azul'])
        self.tarjeta(1, 'UNIDADES VENDIDAS', f'{unidades:,}'.replace(',', '.'), COLORES['azul2'])
        self.tarjeta(2, 'REGISTROS DE VENTA', str(len(self.ventas)), COLORES['naranja'])
        self.tarjeta(3, 'TICKET PROMEDIO', moneda(total / len(self.ventas)), COLORES['azul'])
        self.grafico_linea(por_dia)
        self.grafico_barras(por_producto)
        self.grafico_categoria(por_categoria)

    def lienzo(self, titulo, ancho=350, alto=260):
        marco = tk.Frame(self.graficos, bg='white', highlightbackground=COLORES['borde'], highlightthickness=1)
        marco.pack(side='left', fill='both', expand=True, padx=5)
        tk.Label(marco, text=titulo, bg='white', fg=COLORES['azul'], font=('Arial', 11, 'bold')).pack(pady=(9, 0))
        lienzo = tk.Canvas(marco, bg='white', highlightthickness=0, width=ancho, height=alto)
        lienzo.pack(fill='both', expand=True, padx=8, pady=6)
        return lienzo

    def grafico_linea(self, datos):
        c = self.lienzo('Ventas por día')
        c.update_idletasks(); w=max(c.winfo_width(),340); h=max(c.winfo_height(),245)
        izq, der, arriba, abajo = 48, 15, 18, 38
        valores=list(datos.values()); maximo=max(valores) if valores else 1
        puntos=[]
        for i,(fecha,valor) in enumerate(sorted(datos.items())):
            x=izq+(w-izq-der)*i/max(1,len(datos)-1); y=h-abajo-(h-arriba-abajo)*valor/maximo; puntos.append((x,y))
            c.create_oval(x-4,y-4,x+4,y+4,fill=COLORES['azul2'],outline='white',width=1)
            c.create_text(x,h-20,text=fecha[-5:],font=('Arial',8),fill=COLORES['gris'])
        for i in range(len(puntos)-1): c.create_line(*puntos[i],*puntos[i+1],fill=COLORES['azul2'],width=2)
        for fraccion in (0,.5,1):
            y=h-abajo-(h-arriba-abajo)*fraccion; c.create_line(izq,y,w-der,y,fill='#E8EDF2'); c.create_text(izq-5,y,text=moneda(maximo*fraccion),anchor='e',font=('Arial',7),fill=COLORES['gris'])

    def grafico_barras(self, datos):
        c=self.lienzo('Ventas por producto'); c.update_idletasks(); w=max(c.winfo_width(),340); h=max(c.winfo_height(),245)
        items=sorted(datos.items(),key=lambda x:x[1]); maximo=max(datos.values()) if datos else 1; izq=125; top=18; bottom=12; espacio=(h-top-bottom)/max(1,len(items))
        for i,(nombre,valor) in enumerate(items):
            y=top+i*espacio+4; ancho=(w-izq-18)*valor/maximo; corto=nombre if len(nombre)<19 else nombre[:17]+'…'; c.create_text(izq-6,y+8,text=corto,anchor='e',font=('Arial',8),fill=COLORES['gris']); c.create_rectangle(izq,y,izq+ancho,y+17,fill=COLORES['verde'],outline=''); c.create_text(izq+ancho+4,y+8,text=moneda(valor),anchor='w',font=('Arial',7),fill=COLORES['gris'])

    def grafico_categoria(self, datos):
        c=self.lienzo('Ventas por categoría'); c.update_idletasks(); w=max(c.winfo_width(),340); h=max(c.winfo_height(),245)
        total=sum(datos.values()) or 1; cx,cy=min(w*.35,125),h*.46; radio=min(82,h*.31); inicio=0; colores=[COLORES['azul2'],COLORES['naranja'],COLORES['verde']]
        for i,(nombre,valor) in enumerate(datos.items()):
            extent=360*valor/total; c.create_arc(cx-radio,cy-radio,cx+radio,cy+radio,start=inicio,extent=extent,fill=colores[i%len(colores)],outline='white',width=2); inicio+=extent
        y=55
        for i,(nombre,valor) in enumerate(datos.items()):
            c.create_rectangle(w*.63,y,w*.63+12,y+12,fill=colores[i%len(colores)],outline=''); c.create_text(w*.63+18,y+6,text=f'{nombre}  {valor/total:.0%}',anchor='w',font=('Arial',8),fill=COLORES['gris']); y+=28

    def abrir_registros(self):
        ventana=tk.Toplevel(self); ventana.title('Registros de ventas'); ventana.geometry('900x430'); ventana.configure(bg='white')
        columnas=('Fecha','Producto','Categoría','Ciudad','Vendedor','Unidades','Precio','Total')
        tabla=ttk.Treeview(ventana,columns=columnas,show='headings')
        for col in columnas: tabla.heading(col,text=col); tabla.column(col,width=105,anchor='center')
        for v in self.ventas: tabla.insert('', 'end', values=(v[0],v[1],v[2],v[3],v[4],v[5],moneda(v[6]),moneda(v[5]*v[6])))
        tabla.pack(fill='both',expand=True,padx=12,pady=12)

    def abrir_formulario(self):
        ventana=tk.Toplevel(self); ventana.title('Registrar nueva venta'); ventana.geometry('430x430'); ventana.configure(bg='white')
        tk.Label(ventana,text='Nueva venta',bg='white',fg=COLORES['azul'],font=('Arial',16,'bold')).pack(pady=14)
        campos=['Fecha (AAAA-MM-DD)','Producto','Categoría','Ciudad','Vendedor','Unidades','Precio unitario']; entradas=[]
        for campo in campos:
            fila=tk.Frame(ventana,bg='white'); fila.pack(fill='x',padx=28,pady=4); tk.Label(fila,text=campo,width=20,anchor='w',bg='white').pack(side='left'); e=tk.Entry(fila); e.pack(side='right',fill='x',expand=True); entradas.append(e)
        def guardar():
            try:
                fecha,producto,categoria,ciudad,vendedor= [e.get().strip() for e in entradas[:5]]
                datetime.strptime(fecha,'%Y-%m-%d'); unidades=int(entradas[5].get()); precio=int(entradas[6].get())
                if not all([producto,categoria,ciudad,vendedor]) or unidades<=0 or precio<=0: raise ValueError
                self.ventas.append((fecha,producto,categoria,ciudad,vendedor,unidades,precio)); ventana.destroy(); self.actualizar_dashboard(); messagebox.showinfo('Registro guardado','La venta fue agregada al dashboard.')
            except ValueError: messagebox.showerror('Dato incorrecto','Revisa la fecha, las unidades, el precio y los campos obligatorios.')
        ttk.Button(ventana,text='Guardar venta',command=guardar).pack(pady=18)

if __name__ == '__main__':
    app=Aplicacion()
    app.mainloop()
