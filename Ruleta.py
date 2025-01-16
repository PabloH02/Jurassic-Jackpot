import random

# Definir los números y colores de la ruleta
ruleta = {
    0: 'verde', 
    32: 'rojo', 15: 'negro', 19: 'rojo', 4: 'negro', 21: 'rojo', 2: 'negro', 25: 'rojo', 
    17: 'negro', 34: 'rojo', 6: 'negro', 27: 'rojo', 13: 'negro', 36: 'rojo', 11: 'negro', 
    30: 'rojo', 8: 'negro', 23: 'rojo', 10: 'negro', 5: 'rojo', 24: 'negro', 16: 'rojo', 
    33: 'negro', 1: 'rojo', 20: 'negro', 14: 'rojo', 31: 'negro', 9: 'rojo', 22: 'negro', 
    18: 'rojo', 29: 'negro', 7: 'rojo', 28: 'negro', 12: 'rojo', 35: 'negro', 3: 'rojo', 
    26: 'negro'
}

def girar_ruleta():
    """Simula el giro de la ruleta y devuelve el número y su color."""
    numero_girado = random.choice(list(ruleta.keys()))
    color_girado = ruleta[numero_girado]
    return numero_girado, color_girado

def apostar():
    """Permite al usuario hacer una apuesta."""
    print("Opciones de apuesta:")
    print("1. Apostar a un número específico (0-36)")
    print("2. Apostar al color (rojo/negro)")
    print("3. Apostar a par/impar")
    
    opcion = int(input("Selecciona una opción de apuesta (1/2/3): "))
    
    if opcion == 1:
        numero = int(input("A qué número quieres apostar (0-36): "))
        if numero not in ruleta:
            print("Número no válido.")
            return None
        return {'tipo': 'numero', 'valor': numero}
    
    elif opcion == 2:
        color = input("A qué color deseas apostar (rojo/negro): ").lower()
        if color not in ['rojo', 'negro']:
            print("Color no válido.")
            return None
        return {'tipo': 'color', 'valor': color}
    
    elif opcion == 3:
        par_impar = input("A qué opción deseas apostar (par/impar): ").lower()
        if par_impar not in ['par', 'impar']:
            print("Opción no válida.")
            return None
        return {'tipo': 'par_impar', 'valor': par_impar}
    
    else:
        print("Opción no válida.")
        return None

def verificar_ganador(apuesta, numero, color):
    """Verifica si la apuesta es ganadora."""
    if apuesta['tipo'] == 'numero' and apuesta['valor'] == numero:
        return True
    elif apuesta['tipo'] == 'color' and apuesta['valor'] == color:
        return True
    elif apuesta['tipo'] == 'par_impar':
        if apuesta['valor'] == 'par' and numero % 2 == 0:
            return True
        elif apuesta['valor'] == 'impar' and numero % 2 != 0:
            return True
    return False

def main():
    print("Bienvenido a la ruleta!")
    while True:
        apuesta = apostar()
        if apuesta is None:
            print("Vuelve a intentarlo con una apuesta válida.")
            continue
        
        numero_girado, color_girado = girar_ruleta()
        print(f"La ruleta ha caído en el número {numero_girado} ({color_girado}).")
        
        if verificar_ganador(apuesta, numero_girado, color_girado):
            print("¡Felicidades, ganaste!")
        else:
            print("Lo siento, perdiste.")
        
        otra_apuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if otra_apuesta != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
