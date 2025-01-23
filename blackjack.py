import random

# Crear el mazo de cartas
def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Calcular el valor total de una mano
def calculate_hand_value(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Juego principal de Blackjack
def blackjack():
    print("\n¡Bienvenido al Blackjack!\n")

    deck = create_deck()
    random.shuffle(deck)

    # Repartir cartas iniciales
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Turno del jugador
    while True:
        print(f"Tus cartas: {player_hand} (Total: {calculate_hand_value(player_hand)})")
        print(f"Carta visible del crupier: {dealer_hand[1]}")

        if calculate_hand_value(player_hand) == 21:
            print("\n¡Tienes un Blackjack!\n")
            break

        choice = input("¿Qué quieres hacer? (Pedir/Pasar): ").strip().lower()
        if choice == 'pedir':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                print(f"\nTus cartas: {player_hand} (Total: {calculate_hand_value(player_hand)})")
                print("\nTe pasaste. ¡Pierdes!")
                return
        elif choice == 'pasar':
            break
        else:
            print("Opción inválida, elige 'Pedir' o 'Pasar'.")

    # Turno del crupier
    print("\nTurno del crupier:")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print(f"Cartas del crupier: {dealer_hand} (Total: {calculate_hand_value(dealer_hand)})")

    # Determinar ganador
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        print("\n¡Ganas!")
    elif player_total < dealer_total:
        print("\nPierdes.")
    else:
        print("\nEs un empate.")

if __name__ == "__main__":
    blackjack()