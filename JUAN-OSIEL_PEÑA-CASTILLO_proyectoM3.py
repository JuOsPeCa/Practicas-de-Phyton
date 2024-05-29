import matplotlib.pyplot as plt
import numpy as np

def simular_canicas(num_canicas, num_niveles):
    contenedores = np.zeros(num_niveles + 1)
    
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            if np.random.rand() > 0.5:  # 50% de probabilidad de ir a la derecha
                posicion += 1
        contenedores[posicion] += 1
    
    return contenedores

def graficar_histograma(contenedores):
    plt.bar(range(len(contenedores)), contenedores)
    plt.xlabel('Contenedores')
    plt.ylabel('Cantidad de Canicas')
    plt.title('Simulación de una Máquina de Galton')
    plt.show()

def main():
    num_canicas = 3000
    num_niveles = 12
    
    resultados = simular_canicas(num_canicas, num_niveles)
    graficar_histograma(resultados)

if __name__ == "__main__":
    main()
