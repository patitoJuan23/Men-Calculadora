from tkinter import Button, Tk, Frame, Entry, END, Listbox, Scrollbar, RIGHT, Y, messagebox

# Funciones de la calculadora
def click_boton(valor):
    entrada.insert(END, valor)

def limpiar():
    entrada.delete(0, END)

def calcular():
    try:
        operacion = entrada.get()
        # Verificar si la entrada contiene solo operadores sin números
        if not any(char.isdigit() for char in operacion):
            raise ValueError("Debes introducir números")
        
        resultado = eval(operacion)
        limpiar()
        entrada.insert(END, str(resultado))
        # Agregar la operación y el resultado al historial
        historial.insert(END, f"{operacion} = {resultado}")
    except ValueError as ve:
        messagebox.showwarning("Advertencia", str(ve))
        limpiar()
    except:
        limpiar()
        entrada.insert(END, "Error")

def sumar():
    click_boton("+")

def restar():
    click_boton("-")

def multiplicar():
    click_boton("*")

def dividir():
    click_boton("/")

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora con Historial")

# Campo de entrada
entrada = Entry(root, width=30, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4)

# Marco para los botones
frame = Frame(root)
frame.grid(row=1, column=0, columnspan=4)

# Definición de los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 4, 0), ('-', 4, 2),
    ('*', 5, 0), ('/', 5, 1), ('C', 5, 2),
    ('=', 6, 0, 3)
]

# Función para agregar botones
for (texto, fila, columna, *args) in botones:
    if texto == "=":
        boton = Button(frame, text=texto, width=20, height=2, command=calcular)
    elif texto == "C":
        boton = Button(frame, text=texto, width=10, height=2, command=limpiar)
    elif texto == "+":
        boton = Button(frame, text=texto, width=10, height=2, command=sumar)
    elif texto == "-":
        boton = Button(frame, text=texto, width=10, height=2, command=restar)
    elif texto == "*":
        boton = Button(frame, text=texto, width=10, height=2, command=multiplicar)
    elif texto == "/":
        boton = Button(frame, text=texto, width=10, height=2, command=dividir)
    else:
        boton = Button(frame, text=texto, width=10, height=2, command=lambda valor=texto: click_boton(valor))
    
    boton.grid(row=fila, column=columna, columnspan= args if args else [1])

# Listbox para el historial
scrollbar = Scrollbar(root)
scrollbar.grid(row=0, column=5, rowspan=7, sticky='ns')

historial = Listbox(root, width=30, height=10, yscrollcommand=scrollbar.set)
historial.grid(row=0, column=4, rowspan=7)

scrollbar.config(command=historial.yview)

# Iniciar la ventana
root.mainloop()

