'''
Tema: Autenticar Usuario con bcrypt
Fecha: 08 de septiembre del 2022
Autor: Alejandro Galvez M.
'''
import json
import random
import bcrypt

def contraseñas_usuarios():
    archivo = open('usuarios.txt', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    list = set()
    for mnp in listEst:
        registros = mnp.split(" ")
        tupla=(registros[0], registros[1], registros[2])
        list.add(tupla)
    return list

def estudiantes():
    archivo = open('Estudiantes.prn', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    list = set()
    for mnp in listEst:
        tupla=(mnp[:8], mnp[8:])
        list.add(tupla)
    return list

def materias():
    archivo = open('Kardex.txt', 'r')

    cadena = archivo.read()
    listEst = cadena.split("\n")

    archivo.close()
    conjunto = set()
    for mnp in listEst:
        mnp1 = mnp.split("|")
        tupla=(mnp1[0], mnp1[1], mnp1[2])
        conjunto.add(tupla)
    return conjunto

def listMaterias(ctrl):
    promedios = materias()
    lista_materias = []
    for mat in promedios:
        c, m, p = mat
        if ctrl == c:
            lista_materias.append({"Nombre:":m})
    return json.dumps(lista_materias)

# print(listMaterias("18420447"))

def generar_mayuscula():
    return chr(random.randint(65, 90))

def generar_minuscula():
    return chr(random.randint(97, 122))

def generar_numero():
    return chr(random.randint(48,57))

def generar_caracter():
    caracteres = ['@', '#', '$', '%', '&', '_', '?', '!']
    return caracteres[random.randint(0, 7)]

def generar_contraseña():
    clave = ""
    for i in range(0,10):
        numero = random.randint(1, 5)
        if numero == 1:
            clave = clave + generar_mayuscula()
        elif numero == 2:
            clave = clave + generar_minuscula()
        elif numero == 3:
            clave = clave + generar_caracter()
        elif numero >= 4 and numero <= 5:
            clave = clave + generar_numero()
    return clave

# print(generar_contraseña())

# Cifrar con bcrypt

def cifrar_contraseña(contraseña):
    sal = bcrypt.gensalt()
    contraseña_cifrada = bcrypt.hashpw(contraseña.encode('utf-8'), sal)
    return contraseña_cifrada

# clave = generar_contraseña()
# print(clave, cifrar_contraseña(clave))

def generar_archivo_usuario():
    estudiante = estudiantes()

    usuarios = open('usuarios.txt', 'w')
    contador = 1
    for est in estudiante:
        c, n = est
        clave = generar_contraseña()
        clave_cifrada = cifrar_contraseña(clave)

        registro = c + " " + clave + " " + str(clave_cifrada, 'utf-8') + "\n"
        usuarios.write(registro)
        contador += 1
        print(contador)
    print("Archivo Generado")

# generar_archivo_usuario()

# print(bcrypt.checkpw("97XM&t7Kp9".encode('utf-8'),"$2b$12$VFxFX/6AJK5QkgGZxbWpN.YooN2CCaGYDcSNo3XIMKqI/0AQwrlNq".encode('utf-8')))


