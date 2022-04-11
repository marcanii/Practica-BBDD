from tkinter import *
from tkinter import messagebox
import sqlite3

# ------------------------- Functions -----------------------------

def conexionBBDD():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
		
	try:	
		miCursor.execute('''
			CREATE TABLE DATOSUSUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(20),
			APELLIDO VARCHAR(20),
			PASSWORD VARCHAR(50),
			CORREO VARCHAR(20),
			COMENTARIOS VARCHAR(100))
			''')
		messagebox.showinfo("BBDD","BBDD creada con éxito.")

	except:	
		messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salirApp():
	valor = messagebox.askquestion("Salir","¿Desea salir de la aplicación?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miApellido.set("")
	miPass.set("")
	miCorreo.set("")
	textoComentario.delete(1.0, END)

def crear():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	datos = miNombre.get(),miApellido.get(),miPass.get(),miCorreo.get(),textoComentario.get("1.0", END)
	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
		"','" + miApellido.get() +
		"','" + miPass.get() +
		"','" + miCorreo.get() +
		"','" + textoComentario.get("1.0", END) + "')")
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con éxito")"""
	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
	miConexion.commit()

def leer():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	elUsuario = miCursor.fetchall()
	for usuario in elUsuario:
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miApellido.set(usuario[2])
		miPass.set(usuario[3])
		miCorreo.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	datos = miNombre.get(),miApellido.get(),miPass.get(),miCorreo.get(),textoComentario.get("1.0", END)
	"""miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', APELLIDO='" + miApellido.get() +
		"', PASSWORD='" + miPass.get() +
		"', CORREO='" + miCorreo.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro actualizado con éxito")"""
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, CORREO=?, COMENTARIOS=?" + "WHERE ID=" + miId.get(),(datos))
	miConexion.commit()

def eliminar():
	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro borrado con éxito")

# ------------------------ Main window ----------------------------

root = Tk()
root.title("Práctica BBDD")  # #1c3442
root.iconphoto(False, PhotoImage(file='icon.png'))

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirApp)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUB", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# ----------------------------- Creating Fields ----------------------------------

miFrame = Frame(root)
miFrame.pack()

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miCorreo = StringVar()

cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(justify="center")

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(justify="center")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroApellido.config(justify="center")

cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*", justify="center")

cuadroCorreo = Entry(miFrame, textvariable=miCorreo)
cuadroCorreo.grid(row=4, column=1, padx=10, pady=10)
cuadroCorreo.config(justify="center")

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5,column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# ------------------------------ Here we create the labels -----------------------------------

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

correoLabel = Label(miFrame, text="Correo:")
correoLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# -------------------------- Here the buttons ---------------------------

miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonEliminar = Button(miFrame2, text="Eliminar", command=eliminar)
botonEliminar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()