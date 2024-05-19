#En este proyecto se desarrollo un código donde se solicita al usuario una palabra de mínimo 4 letras y un máximo de 8 letras, si esta condición no se cumple\
#el código concluye, pero si es una palabra que cumple los requisitos el código continua con su ejecución procediendo a la segunda parte la cual es la búsqueda\ 
#de coordenadas dentro de los 4 cuadrantes de un plano cartesiano para imprimir en texto la ubicación de las coordenadas antes ingresadas.

#Parte 1: Longitud de una palabra
def verificar_longitud_palabra(palabra):
    longitud = len(palabra)
    if 4 <= longitud <= 8:
        print("La palabra es correcta. Podemos continuar")
        return True
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras. No puedo continuar")
        return False
    else:
        print(f"Sobran letras. Tiene {longitud} letras. No puedo continuar")
        return False

def obtener_palabra():
    palabra = input("Ingresa una palabra: ")
    return palabra

############################################################################################
#Parte 2: Determinación de cuadrante
def determinar_cuadrante(x, y):
    if x == 0 or y == 0:
        print("La coordenada ingresada es incorrecta. Las coordenadas no pueden ser iguales a 0.")
        return
    if x > 0 and y > 0:
        print("El punto se encuentra en el Cuadrante 1 (Arriba a la Derecha).")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el Cuadrante 2 (Arriba a la Izquierda).")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el Cuadrante 3 (Abajo a la Izquierda).")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el Cuadrante 4 (Abajo a la Derecha).")

def obtener_coordenadas():
    try:
        x = float(input("Ingresa la coordenada X: "))
        y = float(input("Ingresa la coordenada Y: "))
        determinar_cuadrante(x, y)
    except ValueError:
        print("Coordenadas inválidas. Por favor, ingresa números.")

################################################################################################
def main():
    print("Parte 1: Longitud de una palabra")
    palabra = obtener_palabra()
    if verificar_longitud_palabra(palabra):
        print("\nParte 2: Determinación de cuadrante en un plano cartesiano")
        obtener_coordenadas()

if __name__ == "__main__":
    main()


