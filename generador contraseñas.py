__author__ = 'Juan Camilo R'

import secrets
import string

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contraseña = 8
contrasena_generada = generar_contrasena(longitud_contraseña)
print(f"Contraseña generada: {contrasena_generada}")