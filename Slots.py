import random
import time

# Definir los símbolos que aparecerán en los carretes
simbolos = ["🍒", "🍋", "🍊", "🍉", "🔔", "🍇"]

# Función para girar los carretes
def girar_carretes():
    carrete_1 = random.choice(simbolos)
    carrete_2 = random.choice(simbolos)
    carrete_3 = random.choice(simbolos)
    return carrete_1, carrete_2, carrete_3

# Función para mostrar los resultados
def mostrar_resultados(carrete_1, carrete_2, carrete_3):
    print(f"{carrete_1} | {carrete_2} | {carrete_3}")

# Función para verificar si hay una combinación ganadora
def es_ganador(carrete_1, carrete_2, carrete_3):
    if carrete_1 == carrete_2 == carrete_3:
        print("¡Felicidades, has ganado!")
    else:
        print("¡Sigue probando, no has ganado esta vez!")

# Función principal del juego
def jugar():
    print("Bienvenido al juego de slots sin apostar!")
    
    while True:
        try:
            input("Presiona Enter para girar los carretes...")
            
            # Gira los carretes
            carrete_1, carrete_2, carrete_3 = girar_carretes()
            
            # Muestra los resultados
            print("\n¡Los carretes están girando!")
            time.sleep(1)  # Para dar una pequeña pausa y hacer el efecto de giro
            mostrar_resultados(carrete_1, carrete_2, carrete_3)
            
            # Verifica si el jugador ha ganado
            es_ganador(carrete_1, carrete_2, carrete_3)
            
            # Pregunta al jugador si quiere seguir jugando
            jugar_otra_vez = input("\n¿Quieres girar otra vez? (s/n): ").lower()
            if jugar_otra_vez not in ['s', 'n']:
                raise ValueError("Opción inválida, debes escribir 's' o 'n'.")
            if jugar_otra_vez != 's':
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingresa 's' para continuar o 'n' para salir.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")

# Iniciar el juego
if __name__ == "__main__":
    jugar()

    
