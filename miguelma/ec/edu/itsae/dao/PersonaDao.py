# coding:utf-8
'''
Created on 19/1/2015

@author: Miguel Miño
'''

from ec.edu.itsae.conn import DBcon
import json 

class PersonaDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarPersona(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from personas ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada
    
    def insertarPersona(self,nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado):
        con=self.conexion().connect()#solo obtenemos la coneccion
        sql=""" insert into personas(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado  ) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i) """ % (nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado) 
        #3 comillas dobles para poder hacer enter no mas '%s' para asignarle un valor x ser cadena s es de cadena y %i por estado que es un valor numerico  
        #'%s' y %i es para asignar valores s de estring e i de int(entero) y el valor numerico es sin comillas  
        #% (se coloca en orden los parametros) es para ubicar el valor a cada uno en orden de acuerdo lo hemos colocado
        print sql #imprimir de prueba la consulta aqui
        with con:  
            cursor=con.cursor()#conectar con cursor
            cursor.execute(sql)#se ejecuta la consulta
            
    def editarPersona(self,nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado):
        con=self.conexion().connect()
        sql=""" UPDATE personas set(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado  ) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i) """ % (nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
        
        
    def eliminarPersona(self,nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado):
        #con=self.conexion().connect()
        #sql=""" DELETE from personas(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado  ) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i) """ % (nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
        #print sql
        #with con:
        #   cursor=con.cursor()
        #   cursor.execute(sql)
        
        con=self.conexion().connect()
        sql="""DELETE FROM personas WHERE idPersona=6""" 
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
    def buscarPersonaNombre(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select CONCAT(nombre,' ', apell_paterno,' ', apell_materno) as value, idpersona as id from personas where upper(CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        columna=('value' , 'id') #esto es una tupla
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna,row)))                
        return json.dumps(lista, indent=2)
    
    def buscarPersonaDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from personas where upper(CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ %("%"+datobuscado+"%"))
        reporte=con.fetchall()
        return reporte
 
    def validarUsuario(self, usuario, clave):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from trabajador where usuario='%s' and clave='%s' """ %(usuario, clave))
        reporte=con.fetchall()
        return reporte 
        
        