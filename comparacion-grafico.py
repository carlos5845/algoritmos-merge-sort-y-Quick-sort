import time
import random
import matplotlib.pyplot as plt

# Función para realizar la partición del arreglo en Quick Sort
def particion(arreglo, bajo, alto):
    pivote = arreglo[alto]  # Elegir el último elemento como pivote
    i = bajo - 1  # Índice del elemento más pequeño

    # Reorganizar los elementos en torno al pivote
    for j in range(bajo, alto):
        if arreglo[j] <= pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]  # Intercambia elementos

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

# Función para medir el tiempo de ejecución de Quick Sort
def quick_sort_con_tiempo(arreglo):
    tiempo_inicial = time.time()  # Inicia el temporizador
    quick_sort(arreglo, 0, len(arreglo) - 1)  # Ejecuta el algoritmo
    tiempo_final = time.time()  # Finaliza el temporizador
    return tiempo_final - tiempo_inicial  # Retorna el tiempo de ejecución


# Función para fusionar dos subarreglos ordenados en Merge Sort
def fusionar(arreglo, izquierda, medio, derecha):
    tamaño1 = medio - izquierda + 1
    tamaño2 = derecha - medio

    subarreglo_izquierdo = arreglo[izquierda:medio + 1]  # Subarreglo izquierdo
    subarreglo_derecho = arreglo[medio + 1:derecha + 1]  # Subarreglo derecho

    i = j = 0
    k = izquierda

    # Fusionar los dos subarreglos
    while i < tamaño1 and j < tamaño2:
        if subarreglo_izquierdo[i] <= subarreglo_derecho[j]:
            arreglo[k] = subarreglo_izquierdo[i]
            i += 1
        else:
            arreglo[k] = subarreglo_derecho[j]
            j += 1
        k += 1

    # Copiar los elementos restantes
    while i < tamaño1:
        arreglo[k] = subarreglo_izquierdo[i]
        i += 1
        k += 1
    while j < tamaño2:
        arreglo[k] = subarreglo_derecho[j]
        j += 1
        k += 1

# Función recursiva Merge Sort
def merge_sort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        medio = (izquierda + derecha) // 2
        merge_sort(arreglo, izquierda, medio)
        merge_sort(arreglo, medio + 1, derecha)
        fusionar(arreglo, izquierda, medio, derecha)

# Función para medir el tiempo de ejecución de Merge Sort
def merge_sort_con_tiempo(arreglo):
    tiempo_inicial = time.time()  # Inicia el temporizador
    merge_sort(arreglo, 0, len(arreglo) - 1)  # Ejecuta el algoritmo
    tiempo_final = time.time()  # Finaliza el temporizador
    return tiempo_final - tiempo_inicial  # Retorna el tiempo de ejecución


# Generar datos para pruebas y graficar resultados
tamaños = [10, 100, 1000, 10000]
tiempos_quick_sort = []
tiempos_merge_sort = []

# Ejecutar pruebas
for tamaño in tamaños:
    arreglo = [random.randint(0, 10000) for _ in range(tamaño)]

    # Medir tiempo para Quick Sort
    tiempo_qs = quick_sort_con_tiempo(arreglo.copy())
    tiempos_quick_sort.append(tiempo_qs)

    # Medir tiempo para Merge Sort
    tiempo_ms = merge_sort_con_tiempo(arreglo.copy())
    tiempos_merge_sort.append(tiempo_ms)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(tamaños, tiempos_quick_sort, label='Quick Sort', marker='o')
plt.plot(tamaños, tiempos_merge_sort, label='Merge Sort', marker='s')
plt.title('Comparación de tiempos de ejecución de Quick Sort y Merge Sort')
plt.xlabel('Tamaño del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()
