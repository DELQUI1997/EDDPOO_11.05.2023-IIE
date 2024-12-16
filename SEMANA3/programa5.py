from tkinter import *
from tkinter import messagebox ###para importar caja de mensaje en la ventana en caso de errores
ventana =Tk() # sirbe para crear un ventana 
ventana.title("Mi Calculadora")#para poner nombre o encabezado a la ventana 
ventana.geometry("420x280")# para tamaño de ventana ANCHO Y ALTO
ventana.configure(background="blue")# puede ser (background="blue") o (bg="blue") para poner el color de la ventana

#etiquetas se hacen mediante la clase LABEL
#padx y pady es parar separar hay una separacion entre etiquetas y cajas texto
lblPrimerNumero=Label(ventana,text="Primer numero ",background="yellow",foreground="black",font=("arial bold",15))
lblPrimerNumero.grid(column=1, row=1,padx=5,pady=5)#posicion 
lblSegundoNumero=Label(ventana,text="Segundo numero ",background="yellow",foreground="black",font=("arial bold",15))
lblSegundoNumero.grid(column=1, row=2,padx=5,pady=5)#posicion 

#caja texto
txtPrimerNumero= Entry(ventana,font=("arial bold",15),justify=CENTER)#width es el tamaño
txtPrimerNumero.grid(column=2, row=1,padx=5,pady=5)
txtSegundoNumero= Entry(ventana,font=("arial bold",15),justify=CENTER)#width es el tamaño
txtSegundoNumero.grid(column=2, row=2,padx=5,pady=5)

#txtresultado= Entry(ventana,font=("arial bold",15),justify=CENTER)#width es el tamaño
#txtresultado.grid(column=1, row=6,columnspan=2,padx=5,pady=5)

#botones
#funciones
resultado=StringVar() #es una varaiable de tipo string por que se va colocar en una etiqueta
                        #admite cualquier valor como string//sino coloco este objeto no se podria asignar
def suma():#SE NECECITA OBTENER LOS VALORES DE LA CAJA TEXTO se utiliza el comnado GET()
    suma=int(txtPrimerNumero.get())+int(txtSegundoNumero.get())#tmabien se pudo colocar float en vez de int
    return resultado.set(suma)  #set se esta asignando a la variable resultado el valor de suma 
                                #SET=ASIGNAR
def resta():
    resta=int(txtPrimerNumero.get())-int(txtSegundoNumero.get())
    return resultado.set(resta)    
    
def multiplicaion():
    multiplicaion=int(txtPrimerNumero.get())*int(txtSegundoNumero.get())
    return resultado.set(multiplicaion)    

def division():
    try:
        division=int(txtPrimerNumero.get())/int(txtSegundoNumero.get())
        return resultado.set(division)    
    except ZeroDivisionError:##casos 5/0 error
        messagebox.showerror(title="Error",message="La division entre 0 no es permitida")
        ###caja de texto en caso se divida entre cero
        txtPrimerNumero.delete(0,END)## para borrar la informacion del casillero
        txtSegundoNumero.delete(0,END)#para borrar la informacion del casillero
        txtPrimerNumero.focus()# se pide que el cursor se ubique en la caja de texto 1
        
def cerrar():
    ventana.destroy()##para que la ventana se cierre
    
btnsuma=Button(ventana,text="+",bg="green",foreground="white",width=15,font=("arial bold",15),command=suma)
btnsuma.grid(column=1,row=3,padx=5,pady=5)

btnresta=Button(ventana,text="-",bg="green",foreground="white",width=15,font=("arial bold",15),command=resta)
btnresta.grid(column=2,row=3,padx=5,pady=5)
btnmulti=Button(ventana,text="*",bg="green",foreground="white",width=15,font=("arial bold",15),command=multiplicaion)
btnmulti.grid(column=1,row=4,padx=5,pady=5)
btndiv=Button(ventana,text="/",bg="green",foreground="white",width=15,font=("arial bold",15),command=division)
btndiv.grid(column=2,row=4,padx=5,pady=5)

btncerrar=Button(ventana,text="Cerrar",bg="black",foreground="white",font=("arial bold",15),width=35,command=cerrar)
btncerrar.grid(column=1,row=5,columnspan=2,padx=5,pady=5)

lblResultado=Label(ventana,bg="white",width=35,font=("arial bold",15),textvariable=resultado)
###textvariable le dioce a la etiqueta que pueda ser que te asigne la variable "resultado"
lblResultado.grid(column=1, row=6,padx=5,pady=5,columnspan=2)#posicion 


ventana.mainloop()  