import time
import random
# Función para fusionar dos subarreglos ordenados
def fusionar(arreglo, izquierda, medio, derecha):
    # Tamaños de los dos subarreglos a combinar
    tamaño1 = medio - izquierda + 1
    tamaño2 = derecha - medio

    # Crear arreglos temporales
    subarreglo_izquierdo = arreglo[izquierda:medio + 1]  # Subarreglo izquierdo
    subarreglo_derecho = arreglo[medio + 1:derecha + 1]  # Subarreglo derecho

    # Índices iniciales para las sublistas
    i = j = 0
    k = izquierda

    # Combinar los subarreglos en arreglo[izquierda..derecha]
    while i < tamaño1 and j < tamaño2:
        if subarreglo_izquierdo[i] <= subarreglo_derecho[j]:
            arreglo[k] = subarreglo_izquierdo[i]
            i += 1
        else:
            arreglo[k] = subarreglo_derecho[j]
            j += 1
        k += 1

    # Copiar los elementos restantes del subarreglo izquierdo, si hay alguno
    while i < tamaño1:
        arreglo[k] = subarreglo_izquierdo[i]
        i += 1
        k += 1

    # Copiar los elementos restantes del subarreglo derecho, si hay alguno
    while j < tamaño2:
        arreglo[k] = subarreglo_derecho[j]
        j += 1
        k += 1

# Función recursiva Merge Sort (Ordenamiento por mezcla)
def merge_sort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        # Encuentra el punto medio para dividir el arreglo
        medio = (izquierda + derecha) // 2

        # Llamadas recursivas para ordenar las dos mitades
        merge_sort(arreglo, izquierda, medio)
        merge_sort(arreglo, medio + 1, derecha)

        # Fusionar las dos mitades ordenadas
        fusionar(arreglo, izquierda, medio, derecha)

# Función para medir el tiempo de ejecución del Merge Sort
def merge_sort_con_tiempo(arreglo):
    tiempo_inicial = time.time()  # Inicia el temporizador
    merge_sort(arreglo, 0, len(arreglo) - 1)  # Ejecuta el algoritmo
    tiempo_final = time.time()  # Finaliza el temporizador
    return tiempo_final - tiempo_inicial  # Retorna el tiempo de ejecución
# Generar arreglos de diferentes tamaños
tamaños = [10, 100, 1000, 10000]
for tamaño in tamaños:
    arreglo = [random.randint(0, 10000) for _ in range(tamaño)]  # Crear un arreglo aleatorio
    tiempo_ejecucion = merge_sort_con_tiempo(arreglo.copy())  # Mide el tiempo de ejecución
    print(f"Merge Sort - Tamaño del arreglo: {tamaño}, Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")