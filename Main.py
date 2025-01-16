def mostrar_menu():
    print("\nBienvenido al Casino Jurassic Jackpot")
    print("Selecciona una opción para jugar:")
    print("1. Jugar a la Ruleta")
    print("2. Jugar al Blackjack")
    print("3. Jugar a la Tragaperras")
    print("4. Jugar a los Dados")
    print("5. Salir")

def jugar_ruleta():
    print("\n¡Has elegido jugar a la Ruleta!")
    # Aquí puedes agregar la lógica del juego de la ruleta
    print("La ruleta está girando...")

def jugar_blackjack():
    print("\n¡Has elegido jugar al Blackjack!")
    # Aquí puedes agregar la lógica del juego de Blackjack
    print("¡Tus cartas han sido repartidas!")

def jugar_tragaperras():
    print("\n¡Has elegido jugar a la Tragaperras!")
    # Aquí puedes agregar la lógica de las tragaperras
    print("¡La máquina está girando...!")

def jugar_dados():
    print("\n¡Has elegido jugar a los Dados!")
    # Aquí puedes agregar la lógica del juego de dados
    
    print("¡Tira los dados y veamos qué sale!")

def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la opción que deseas elegir: ")
        
        if opcion == '1':
            jugar_ruleta()
        elif opcion == '2':
            jugar_blackjack()
        elif opcion == '3':
            jugar_tragaperras()
        elif opcion == '4':
            jugar_dados()
        elif opcion == '5':
            print("\nGracias por jugar en el Casino Jurassic Jackpot. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
