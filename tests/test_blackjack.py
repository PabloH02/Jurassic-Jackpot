import random

# Función para tratar los ases que pueden tener valor como 1 u 11
def obtenerValorCarta(carta, jugada):
    if carta == 1:
        return 11 if jugada + 11 <= 21 else 1
    return carta
# Define el juego para poder repetirlo
def jugar():
    # Inicializamos las cartas
    krupier1 = random.randint(1, 10)
    krupier2 = random.randint(1, 10)
    if krupier1 == 1 or krupier2 == 1:
        krupier1 = obtenerValorCarta(krupier1, krupier1 + krupier2)
        krupier2 = obtenerValorCarta(krupier2, krupier1 + krupier2)

    jugadaKrupier = krupier1 + krupier2
    carta1 = random.randint(1, 10)
    carta2 = random.randint(1, 10)
    jugada = obtenerValorCarta(carta1, 0) + obtenerValorCarta(carta2, 0)

    print(f"Tus cartas son {carta1} y {carta2} :: {jugada}")
    print(f"El krupier tiene {krupier1}")
    # Funcion para pedir cuantas cartas quiera
    def pedirCarta(jugada):
        carta = random.randint(1, 10)
        valor_carta = obtenerValorCarta(carta, jugada)
        print(f"Te ha salido un {carta}")
        jugada += valor_carta
        if jugada > 21:
            return "Mayor que 21, has perdido"
        return jugada
    # Funcion para ver la jugada del krupier
    def krupier(jugadaKrupier):
        while jugadaKrupier < 16:
            carta = random.randint(1, 10)
            valor_carta = obtenerValorCarta(carta, jugadaKrupier)
            print(f"Le ha salido {carta}")
            jugadaKrupier += valor_carta
        return jugadaKrupier
    
    while True:
        try:
                condicion = int(input('Elija su jugada: \n1.Pedir \n2.Quedarse\n'))
        except ValueError:
                print("Por favor, introduce un número válido.")
                continue
        if condicion == 1:
            jugada = pedirCarta(jugada)
            print(f"Tu jugada es {jugada}")
            if isinstance(jugada, str):  # Si la jugada es una cadena
                print(jugada)
                break
        elif condicion == 2:
            jugadaKrupier = krupier(jugadaKrupier)
            print(f"El krupier tiene:{jugadaKrupier}")
            if jugada > jugadaKrupier and jugada <= 21 or jugadaKrupier>21:
                print('Has ganado')
            else:
                print('Has perdido')
            break
        else:
            print("No has elegido una opción correcta")
    
    
    jugar_de_nuevo = input("¿Quieres jugar otra vez? (s/n): ")
    if jugar_de_nuevo == 's':
        jugar()  # Vuelve a jugar
    else:
        print("¡Gracias por jugar!")

# Iniciar el juego
jugar()
