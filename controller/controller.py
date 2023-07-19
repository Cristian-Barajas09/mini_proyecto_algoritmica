from model.model import Model
from typing import Tuple,Any
class Controller:
    def __init__(self):
        self.conn = Model()


    def set_huesped(self,cedula:int,apellido:str,nombre:str,direccion:str,ciudad:str,email:str,telefono:str) -> int | str:

        if '@' in email:
            return "formato de correo no valido"

        return self.conn.set_huesped(cedula=cedula,apellido=apellido,nombre=nombre,direccion=direccion,telefono=telefono,ciudad=ciudad)

    def get_huespedes(self) -> tuple[Tuple[Any,...],...]:
        return self.conn.get_huespedes()

    def del_huesped(self,cedula:int) -> int:
        return self.conn.del_huesped(cedula=cedula)

    def update_huesped(self,cedula:int,old_cedula:int,apellido:str,nombre:str,direccion:str,ciudad:str,email:str,telefono:str) -> int :
        return self.conn.update_husped(cedula,old_cedula,apellido,nombre,direccion,ciudad,email,telefono)

    def get_huesped(self,cedula:int) -> int:
        return self.conn.get_huesped(cedula=cedula)

