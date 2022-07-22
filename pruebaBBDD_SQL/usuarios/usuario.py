import hashlib
from sqlite3 import connect
from usuarios import conexion
from datetime import datetime

#Llamar a la FUNCIÓN -"def conectar" en el ARCHIVO "Conexión.py":
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        now = datetime.now()
        fecha = now.strftime("%Y/%m/%d")
        
        #Cifrar Password:
        passwordEncode = self.password.encode('utf8')
        cifrado = hashlib.sha256()
        cifrado.update(passwordEncode)
        passwordEncodeFinal = cifrado.hexdigest()
        
        usuario = (self.nombre, self.apellidos, self.email, passwordEncodeFinal, fecha)
        sql = ("INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)")
        
        try:
            cursor.execute(sql,usuario)
            database.commit()
            return [cursor.rowcount, self]
        except:
            result = [0,self]
        
        return result
    
    def identificar(self):
        
        #Consulta para comprobar si existe el usuario:
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #Cifrar Password:
        passwordEncode = self.password.encode('utf8')
        cifrado = hashlib.sha256()
        cifrado.update(passwordEncode)
        passwordEncodeFinal = cifrado.hexdigest()
        
        #Datos para la consulta:
        usuario = (self.email, passwordEncodeFinal)
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result