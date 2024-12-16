\import tkinter as tk
from tkinter import messagebox

def submit_form():
    first_name = entry_first_name.get()
    second_name = entry_second_name.get()
    first_lastname = entry_first_lastname.get()
    second_lastname = entry_second_lastname.get()
    
    # Validación de campos vacíos
    if first_name == '' or first_lastname == '':
        messagebox.showerror('Error', 'Todos los campos son obligatorios')
        return
    
    messagebox.showinfo('Datos personales', f'Primer nombre: {first_name}\nSegundo nombre: {second_name}\nPrimer Apellido: {first_lastname}\nSegundo apellido: {second_lastname}')

def clear_form():
    entry_first_name.delete(0, tk.END)
    entry_second_name.delete(0, tk.END)
    entry_first_lastname.delete(0, tk.END)
    entry_second_lastname.delete(0, tk.END)


window = tk.Tk()
window.title('DATOS PERSONALES')

label_title = tk.Label(window, text='DATOS PERSONALES', font=('Arial', 12, 'bold'))
label_title.grid(row=0, columnspan=2, padx=12, pady=12)

label_first_name = tk.Label(window, text='Primer Nombre:')
label_first_name.grid(row=1, column=0, padx=12, pady=12)
entry_first_name = tk.Entry(window)
entry_first_name.grid(row=1, column=1, padx=12, pady=12)


label_second_name = tk.Label(window, text='Segundo Nombre:')
label_second_name.grid(row=2, column=0, padx=12, pady=12)
entry_second_name = tk.Entry(window)
entry_second_name.grid(row=2, column=1, padx=12, pady=12)


label_first_lastname = tk.Label(window, text='Primer Apellido:')
label_first_lastname.grid(row=3, column=0, padx=12, pady=12)
entry_first_lastname = tk.Entry(window)
entry_first_lastname.grid(row=3, column=1, padx=12, pady=12)

label_second_lastname = tk.Label(window, text='Segundo Apellido:')
label_second_lastname.grid(row=4, column=0, padx=12, pady=12)
entry_second_lastname = tk.Entry(window)
entry_second_lastname.grid(row=4, column=1, padx=12, pady=12)


gray_bar = tk.Frame(window, height=10, bg='gray')
gray_bar.grid(row=5, columnspan=2, sticky='ew', padx=12, pady=12)

button_submit = tk.Button(window, text='Enviar', command=submit_form, width=12)
button_submit.grid(row=6, column=0, padx=12, pady=12)
button_clear = tk.Button(window, text='Limpiar', command=clear_form, width=12)
button_clear.grid(row=6, column=1, padx=12, pady=12)

window.mainloop()