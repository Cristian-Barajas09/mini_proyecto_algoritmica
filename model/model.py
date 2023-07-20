import pymysql.connections
from pymysql.cursors import Cursor
from configs.configs import Config
class Model :
    def __init__(self):
        config = Config()
        self.__keys = config.getKeys()


    def connect(self):
        con = pymysql.connect(**self.__keys)
        return con

    def query(func):
        def intern(self,*args,**kwargs):
            con = Model().connect()
            cur = con.cursor()
            func(self,con,cur,*args,**kwargs)
            con.close()
        return intern

    @query
    def get_huespedes(self,con,cur: Cursor):
        cur.execute("SELECT * FROM huesped")
        result = cur.fetchall()
        return result

    @query
    def set_huesped(self,con,cur: Cursor,cedula:int,apellido:str,nombre:str,direccion:str,ciudad:str,email:str,telefono:str):
        cur.execute(f"INSERT INTO huesped (ced_hue,ape_hue,nom_hue,dir_hue,ciu_hue,email_hue,tel_hue) VALUES ({cedula},'{apellido}','{nombre}','{direccion}','{ciudad}','{email}','{telefono}')")
        con.commit()
        result = cur.rowcount
        return result

    @query
    def del_huesped(self,con,cur:Cursor,cedula:int):
        cur.execute(f"DELETE FROM huesped WHERE ced_hue = {cedula}")
        con.commit()
        result = cur.rowcount
        return result

    @query
    def update_husped(self,con,cur:Cursor,cedula:int,old_cedula:int,apellido:str,nombre:str,direccion:str,ciudad:str,email:str,telefono:str):
        cur.execute(f"UPDATE huesped SET ced_hue={cedula},ape_hue={apellido},nom_hue={nombre},dir_hue={direccion},ciu_hue={ciudad},email_hue={email},tel_hue={telefono} WHERE ced_hue= {old_cedula}")
        con.commit()
        result = cur.rowcount
        return result

    @query
    def get_huesped(self,con,cur:Cursor,cedula:int):
        cur.execute(f"SELECT * FROM huesped WHERE ced_hue = {cedula}")
        con.commit()
        result = cur.fetchone()

        return result

    @query
    def set_habitacion(self,con,cur:Cursor,codigo:int | str,numero:int,tipo:str,capacidad:str,precio:float,status:str) -> int:
        """
            metodo para crear las habitaciones
            :param con: conexion a la base de datos esta viene por el decorador query
            :param cur: cursor de la base de datos este viene por el decorador query
            :param codigo: 
        """
        cur.execute(f"INSERT INTO habitacion (cod_hab,num_hab,tip_hab,cap_hab,pre_hab,sta_hab) VALUES ('{codigo}','{numero}','{tipo}','{capacidad}',{precio},'{status}')")
        con.commit()

        result = cur.rowcount
        return result

    @query
    def update_habitacion(self,con,cur:Cursor,codigo:int | str,old_codigo,numero:int,tipo:str,capacidad:str,precio:float,status:str):
        cur.execute(f"UPDATE habitacion SET cod_hab='{codigo}',num_hab='{numero}',tip_hab='{tipo}',cap_hab='{capacidad}',pre_hab={precio},sta_hab='{status}' WHERE cod_hab={old_codigo}")
        con.commit()
        result = cur.rowcount
        return result

    @query
    def del_habitacion(self,con,cur: Cursor,codigo):
        cur.execute(f"DELETE FROM habitacion WHERE cod_hab={codigo}")
        con.commit()
        result = cur.rowcount
        return result
