# 1 - Edad usuario:

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")



# 2 - Nota usuario: 

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")



# 3 - Numeros pares:

while True:
  try:
    numero = int(input("Ingrese un número par: "))
    if numero % 2 == 0:
      print("Ha ingresado un número par")
      break  # Sale del bucle si el número es par
    else:
      print("Por favor, ingrese un número par")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")



# 4 - Edad usuario: 

edad = int(input("Ingrese su edad: "))

if edad < 12:
  print("Niño/a")
elif edad >= 12 and edad < 18:
  print("Adolescente")
elif edad >= 18 and edad < 30:
  print("Adulto/a joven")
else:
  print("Adulto/a")



# 5 - Programa contraseñas: 

cadena = "Hola, mundo!"
longitud_cadena = len(cadena)  # longitud_cadena será 13

lista = [1, 2, 3, 4, 5]
longitud_lista = len(lista)  # longitud_lista será 5



# 6 - Programa estadistico:

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
  print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
  print("Sesgo negativo o a la izquierda")
else:
  print("Sin sesgo")



# 7 - Escribir un programa que solicite una frase o palabra al usuario:

frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
  frase += "!"

print(frase)


# 8 - Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3:

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1, 2 o 3 dependiendo de la opción que desee: "))

if opcion == 1:
  print(nombre.upper())
elif opcion == 2:
  print(nombre.lower())
elif opcion == 3:
  print(nombre.title())
else:
  print("Opción no válida")


# 9 - Clasificacion de magnitud del terremoto.

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
  print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
  print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")
else:
  print("Extremo (puede causar graves daños a gran escala)")



# 10 - Determina la estación del año según el hemisferio, mes y día.

def determinar_estacion(hemisferio, mes, dia):
    """Determina la estación del año según el hemisferio, mes y día.

    Args:
        hemisferio (str): 'N' para hemisferio norte, 'S' para hemisferio sur.
        mes (str): Nombre del mes.
        dia (int): Día del mes.

    Returns:
        str: La estación del año en ese hemisferio y fecha, o un mensaje de error si la entrada es inválida.
    """

    mes = mes.lower()

    if hemisferio.upper() == 'N':
        if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
            return "Invierno"
        elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
            return "Primavera"
        elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
            return "Verano"
        elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
            return "Otoño"
        else:
            return "Fecha inválida para el hemisferio norte."
    elif hemisferio.upper() == 'S':
        if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
            return "Verano"
        elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
            return "Otoño"
        elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
            return "Invierno"
        elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
            return "Primavera"
        else:
            return "Fecha inválida para el hemisferio sur."
    else:
        return "Hemisferio inválido. Por favor, ingrese 'N' o 'S'."

# Solicitar información al usuario
hemisferio_usuario = input("¿En qué hemisferio se encuentra? (N/S): ")
mes_usuario = input("¿Qué mes del año es?: ")
dia_usuario = int(input("¿Qué día del mes es?: "))

# Determinar e imprimir la estación
estacion = determinar_estacion(hemisferio_usuario, mes_usuario, dia_usuario)
print(f"En el hemisferio {hemisferio_usuario.upper()} el {dia_usuario} de {mes_usuario.capitalize()} es {estacion}.")