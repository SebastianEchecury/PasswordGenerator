import random

def generarContraseña(largoPW):
    pw = ''
    for x in range(largoPW):
        caracteres = 'abcdefghijklmnñopqrstuvxyzABCDEFGHIJKLMÑOPQRSTUVXYZ0123456789!?&%$#@\/()'
        caracter = caracteres[random.randint(0, len(caracteres)-1)]
        pw += caracter
    return pw


print ('Ingrese cantidad de contraseñas a generar: ', end='')
cantPW = int(input())

print('Ingrese longitud de contraseñas: ', end='')
largoPW = int(input())

for x in range(cantPW):
    print(generarContraseña(largoPW))

