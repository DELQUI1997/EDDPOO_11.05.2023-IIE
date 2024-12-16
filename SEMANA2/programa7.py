from tkinter import * #se imprta todas las variables ,modulos tenga la libreria tkinter

ventana=Tk() # es una clase ,,un modulo tiene funciones y clases tk() es una clase
                # se crea una objeto de la clase tk()
                # todas las clase empieza con mayuscula 
ventana.title("Mi ventana") #se coloca un titulo en la ventana
ventana.geometry("750x200")#tamaño de la ventana
etiqueta=Label(ventana,text="Hola...",font=("Arial bold",20)) #la clase LABEL / se puede coplocar un texto
#la etiqueta se crea a travez de la clase label()
#font se coloca un tipo de fuente a la etiqueta y luego el tamaño
etiqueta.grid(column=0, row=0)#posicion 

def click():
    etiqueta.configure(text="Hiciste click---!!!") #a la etiqueta se cambiaria el texto 

boton=Button(ventana,text="Click aqui..!!!",bg="orange",foreground="red",command=click)#se llama a la clase button
#, se coloca un texto , un color bg=el fondo del boton, foreground el color de texto del boton
#command se llama a la funcion click
boton.grid(column=1,row=0)#posicion del boton
#padx espacios entre la etiqiutea y el boton de manera horizontal de izq a der
#pady espacios entre la etiqiutea y el boton de manera vertical de arriba a abajo

##se crea un objeto una caja de texto
texto= Entry(ventana,width=20)#width es el tamaño
texto.grid(column=2, row=0)


ventana.mainloop() # es para que se pueda mostrar la ventana
#la clase tk() pemrmite la creacion de esta ventana
# se importo un modulo TKINTER todo sus variables dfunciones etc *
