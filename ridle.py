import random

def adivina_el_numero():
    numero_aleatorio = random.randint(1, 100)
    adivinanza = None   
    
    print("----------------------------")
    print("Bienvenido al juego de adivinzas del número")
    print("----------------------------")
    print("¿Adivinaras el numero que he seleccionado?")

    while adivinanza != numero_aleatorio:
        try:
            adivinanza = int(input("Introduce un numero entre 1 y 100: "))
            
            if adivinanza < 1 or adivinanza > 100:
                print("Introduzca un rango entre 1 al 100.")
            elif adivinanza < numero_aleatorio:
                print("Intente de nuevo. EL numero es muy pequeño.")
            elif adivinanza > numero_aleatorio:
                print("Intente de nuevo. El numero es muy grande")
            else:
                print("Felicidades, acerto el número")
        except ValueError:
            print("Por favor, introduce un número valido.")
        

adivina_el_numero()
