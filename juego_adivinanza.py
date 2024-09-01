

import random


numero_secreto = random.randint(0,100)
cantidad_intentos = 0
cant_max_intentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el numero secreto!")

while not adivinado and cantidad_intentos < cant_max_intentos:
    entrada = input("Introduce un numero de 1 al 99: ") 
    numero = int(entrada)
    if numero == numero_secreto:
        print("Felicitaciones, adivinaste el numero secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado!")
    else:
        print("El numero es menor al ingresado!")
    cantidad_intentos += 1
if not cantidad_intentos < cant_max_intentos:
    print("Game Over, No has podido adivinar dentro del numero permitido de intentos!")