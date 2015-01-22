#coding: utf-8 
'''
Created on 19/1/2015

@author: PC30
'''
from app import app
from ec.edu.itsae.dao import PersonaDao
from flask import render_template, request, redirect, url_for

@app.route("/mainpersona")
def personamain():
    objR=PersonaDao.PersonaDao().reportarPersona()#llamar al reporte
    return render_template("prueba.html", data=objR)#enviando al archivo html y ahi organizarlo

@app.route("/addPersona", methods=['post'])
def addPersona():
    nombre=request.form.get('nombre', type=str) #request para capturar los valores del html
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)
    
    PersonaDao.PersonaDao().insertarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('personamain'))

    PersonaDao.PersonaDao().editarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('personamain'))

    PersonaDao.PersonaDao().eliminarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('personamain'))


@app.route("/buscarauto")
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objR=PersonaDao.PersonaDao().buscarPersonaNombre(nombre)
    print objR
    
    return objR

@app.route("/buscarDato")
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=PersonaDao.PersonaDao().buscarPersonaDato(nombre)
    return render_template("prueba.html", data=objR)
