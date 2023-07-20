from tkinter import *

root = Tk()
root.title("Formulario")
root.geometry("400x600")
root.resizable(False,False)

#Marco Principal
main_frame = Frame(root,border=4, relief="ridge",background="#213141",
width=400,height=600)
main_frame.place(x=0,y=0)

#Encabezado
main_title = Label(main_frame,text="Registro del hotel",
                font=("Cambria",12),
                bg= "#B5C7DF")
main_title.place(x=138,y=30,width=125)

#keys
cedula = IntVar
name_lastname= StringVar
direction = StringVar
city = StringVar
email = StringVar
phone = IntVar


#Label que ya odio escribir; Pd: el orden puede variar
cedula_label = Label(text="Cedula").pack()
cedula_label = Entry(textvariable = cedula ,border = 2,relief="ridge").pack()

name_lastname_label = Label(text="Nombre y Apellido").pack()
name_lastname_label = Entry().pack()


direction_label = Label(text="Direccion").pack()
direction_label = Entry().pack()

city_label = Label(text="Ciudad")
city_label = Entry().pack()

email_label = Label(text="Email")
email_label = Entry().pack()

phone_label = Label(text="Telefono")
phone_label = Entry().pack()





root.mainloop()