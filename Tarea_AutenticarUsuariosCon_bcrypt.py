'''
Tema: Autenticar Usuario con bcrypt
Fecha: 08 de septiembre del 2022
Autor: Alejandro Galvez M.
'''

from practica7 import *
import bcrypt

def autenticar_usuario(usuario, contrasena):
    registro = contraseñas_usuarios()
    estudiante = estudiantes()
    autenticacion = {}
    for reg in registro:
        if reg[0] == usuario:
            for est in estudiante:
                if est[0]==usuario:
                    ban = bcrypt.checkpw(contrasena.encode('utf-8'), reg[2].encode('utf-8'))
                    autenticacion["Bandera"] = ban
                    autenticacion["Usuario"] = est[1]
                    if ban:
                        autenticacion["Mensaje"] = "Bienvenido al Sistema de Autenticación de usuarios"
                    else:
                        autenticacion["Mensaje"] = "Contraseña incorrecta"
                    return autenticacion
    autenticacion["Bandera"] = False
    autenticacion["Usuario"] = ""
    autenticacion["Mensaje"] = "No existe el Usuario"
    return autenticacion

print(autenticar_usuario("18420447","1GVF3xLk0W"))
