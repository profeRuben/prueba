import random

print("¡Bienvenido a la Isla Aleatoria!")

inicio = int(input("Ingrese el límite inferior del rango de zonas: "))
fin = int(input("Ingrese el límite superior del rango de zonas: "))

while inicio >= fin:
    print("El límite inferior debe ser menor que el límite superior. Intente nuevamente.")
    inicio = int(input("Ingrese el límite inferior del rango de zonas: "))
    fin = int(input("Ingrese el límite superior del rango de zonas: "))

intentos_max = int(input("¿Cuántos intentos desea tener?: "))

zona_tesoro = random.randint(inicio, fin)
intento = 1
acertado = False

while intento <= intentos_max:
    eleccion = int(input(f"Intento {intento} - Elige una zona: "))
    
    if eleccion == zona_tesoro:
        print("¡Tesoro encontrado! ¡Felicidades, pirata!")
        acertado = True
        break
    elif intento == 2:
        distancia = abs(eleccion - zona_tesoro)
        if distancia < 3:
            print("Muy cerca...")
        else:
            print("Muy lejos...")
    
    intento += 1

if not acertado:
    print("El tesoro seguirá perdido por siempre...")
