import time
import random

# Función para realizar la partición del arreglo
def particion(arreglo, bajo, alto):
    pivote = arreglo[alto]  # Elegir el último elemento como pivote
    i = bajo - 1  # Índice del elemento más pequeño

    # Reorganizar los elementos en torno al pivote
    for j in range(bajo, alto):
        if arreglo[j] <= pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]  # Intercambia elementos si son menores o iguales al pivote

    # Colocar el pivote en su posición correcta
    arreglo[i + 1], arreglo[alto] = arreglo[alto], arreglo[i + 1]
    return i + 1

# Función recursiva Quick Sort
def quick_sort(arreglo, bajo, alto):
    if bajo < alto:
        # Encontrar el índice de partición
        indice_pivote = particion(arreglo, bajo, alto)

        # Llamadas recursivas para ordenar las dos particiones
        quick_sort(arreglo, bajo, indice_pivote - 1)  # Subarreglo izquierdo
        quick_sort(arreglo, indice_pivote + 1, alto)  # Subarreglo derecho

# Función para medir el tiempo de ejecución del Quick Sort
def quick_sort_con_tiempo(arreglo):
    tiempo_inicial = time.time()  # Inicia el temporizador
    quick_sort(arreglo, 0, len(arreglo) - 1)  # Ejecuta el algoritmo
    tiempo_final = time.time()  # Finaliza el temporizador
    return tiempo_final - tiempo_inicial  # Retorna el tiempo de ejecución

# Generar arreglos de diferentes tamaños
tamaños = [10, 100, 1000, 10000]
for tamaño in tamaños:
    arreglo = [random.randint(0, 10000) for _ in range(tamaño)]  # Crear un arreglo aleatorio
    tiempo_ejecucion = quick_sort_con_tiempo(arreglo.copy())  # Mide el tiempo de ejecución
    print(f"Quick Sort - Tamaño del arreglo: {tamaño}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
