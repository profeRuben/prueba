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
tu_mejor_distancia = 1000

while intento <= intentos_max:
    eleccion = int(input(f"Intento {intento} - Elige una zona: "))
    
    if eleccion == zona_tesoro:
        print("¡Tesoro encontrado! ¡Felicidades, pirata!")
        acertado = True
        break
    else:
        #calcula el número absoluto de la diferencia (siempro positivo)
        distancia = abs(eleccion - zona_tesoro)
        if distancia < tu_mejor_distancia:
            tu_mejor_intento = distancia
        if distancia < 3:
            print("Muy cerca...")
        else:
            print("Muy lejos...")
    intento += 1

if not acertado:
    print(f" El número era: {zona_tesoro}. El tesoro seguirá perdido por siempre...")
    print(f" Tu distancia mas cercana fué: {tu_mejor_intento}")
