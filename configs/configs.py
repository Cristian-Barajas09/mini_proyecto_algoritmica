from dotenv import dotenv_values

import os
import tkinter as tk

from tkinter.messagebox import showerror
from pymysql.cursors import DictCursor

config = dotenv_values(".env")




class ViewKeys(tk.Frame):
    def __init__(self,window: tk.Tk = None):
        super().__init__(window,width=400,height=100)
        self.window = window
        self.key_entry()
        self.pack()


    def key_entry(self):


        label1 = tk.Label(self.window,text="Por favor ingrese los datos para ingresar en la base de datos",)
        label1.pack()

        label2 = tk.Label(self.window,text="Host: ")
        label2.pack()

        self.input1 = tk.Entry(self.window,textvariable=self.input_text("localhost"))
        self.input1.pack()

        label3 = tk.Label(self.window,text="Usuario : ")
        label3.pack()

        self.input2 = tk.Entry(self.window,textvariable=self.input_text("root"))
        self.input2.pack()

        label4 = tk.Label(self.window,text="Puerto: ")
        label4.pack()

        self.input3 = tk.Entry(self.window,textvariable=self.input_text("3306"))
        self.input3.pack()



        label5 = tk.Label(self.window,text="Contraseña (opcional): ")
        label5.pack()
        self.input4 = tk.Entry(self.window,show="*")
        self.input4.pack()
        self.btn1 = tk.Checkbutton(self.window,text="mostrar contraseña",command=self.mostrarClave)
        self.btn1.pack(pady=10)

        label6 = tk.Label(self.window,text="nombre de la base de datos: ")
        label6.pack()
        self.input5 = tk.Entry(self.window,textvariable=self.input_text("test"))
        self.input5.pack()


        btn2 = tk.Button(self.window,text="guardar",command=self.crear_variables)
        btn2.pack(pady=10)

        label6 = tk.Label(self.window,text="el programa se cerrara, por favor volver a ejecutar despues de precionar el boton")
        label6.pack()


    def input_text(self,texto:str) -> tk.Variable:
        variable_text = tk.Variable(self.window,texto)
        return variable_text

    def crear_variables(self):
        host = self.input1.get()
        usuario = self.input2.get()
        puerto = self.input3.get()
        database = self.input5.get()
        if self.input4.get() != "":
            clave = self.input4.get()
        if os.path.exists(os.path.join(os.path.dirname(__file__),".env")):
            os.remove(os.path.join(os.path.dirname(__file__),".env"))
            self.crear_variables()
        else:
            with open(".env","w+") as file:
                file.write("# KEYS FOR DATABASE\n")
                file.write(f"HOST_DATABASE = {host}\n")
                file.write(f"USER_DATABASE = {usuario}\n")
                file.write(f"PORT_DATABASE = {puerto}\n")
                file.write(f"NAME_DATABASE = {database}\n")

                if self.input4.get() != "":
                    file.write(f"PASSWORD_DATABASE = {clave}\n")

                self.window.destroy()
    def mostrarClave(self):
        if self.input4.cget("show") == "*":
            self.input4.config(show="")
        else :
            self.input4.config(show="*")




def run():
    window = tk.Tk()
    window.wm_title("guardar variables de entorno")
    app = ViewKeys(window)
    app.mainloop()


class Config:

    def __init__(self):
        try:
            self.keys_db = {
                "host": config['HOST_DATABASE'],
                "user": config['USER_DATABASE'],
                "port": int(config['PORT_DATABASE']),
                "database": config['NAME_DATABASE'],
                "cursorclass": DictCursor
            }
            if config['PASSWORD_DATABASE']:
                self.keys_db["password"] = config['PASSWORD_DATABASE']

        except KeyError as error:
            showerror("error","no se encontraron las variables de entorno")
            run()


    def getKeys(self):
        return self.keys_db





if __name__ == "__main__":
    keys_db = Config()
