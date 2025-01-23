import Dados
import Ruleta
import Slots
import Blackjack

def mostrar_menu():
    print("\nBienvenido al Casino Jurassic Jackpot")
    print("Selecciona una opción para jugar:")
    print("1. Jugar a la Ruleta")
    print("2. Jugar al Blackjack")
    print("3. Jugar a la Slot")
    print("4. Jugar a los Dados")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce el número de la opción que deseas elegir: ")
        
        if opcion == '1':
            Ruleta.juegoRuleta()
        elif opcion == '2':
            Blackjack.juegoBlackjack()
        elif opcion == '3':
            Slots.juegoSlots()
        elif opcion == '4':
            Dados.juegoDados()
        elif opcion == '5':
            print("\nGracias por jugar en el Casino Jurassic Jackpot. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
