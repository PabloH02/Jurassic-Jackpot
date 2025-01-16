import random

# Función para lanzar los dados
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función principal del juego
def juegoDados():
    print("¡Bienvenido al juego de dados del casino!")
    
    # El jugador elige si cree que la suma de los dados será mayor o menor que 7
    eleccion = input("¿Crees que la suma de los dados será mayor o menor que 7? (mayo/meno): ").lower()
    
    if eleccion not in ["mayo", "meno"]:
        print("Opción no válida. Debes elegir 'mayo' o 'meno'.")
        return

    # Lanzamos los dados
    dado1, dado2 = lanzar_dados()
    suma_dados = dado1 + dado2
    print(f"Los dados muestran: {dado1} y {dado2}. La suma es {suma_dados}.")

    # Verificamos si el jugador ganó o perdió
    if (eleccion == "mayo" and suma_dados > 7) or (eleccion == "meno" and suma_dados < 7):
        print(f"¡Ganaste! La suma fue {suma_dados}.")
    else:
        print(f"Perdiste. La suma fue {suma_dados}.")


