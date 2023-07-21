import random
import time
import matplotlib.pyplot as plt
import tkinter as tk

# Implementación de los algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return time.time() - start_time, arr

def selection_sort(arr):
    longitud = len(arr)
    start_time = time.time()
    for i in range(longitud - 1):
        for j in range(i + 1, longitud):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return time.time() - start_time, arr

def insert_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return time.time() - start_time, arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    start_time = time.time()
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2
    return time.time() - start_time, arr

def merge_sort(arr):
    def merge(arr, left, mid, right):
        i = left
        j = mid + 1
        k = 0
        temp = [0] * (right - left + 1)
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(right - left + 1):
            arr[left + i] = temp[i]

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

    n = len(arr)
    start_time = time.time()
    merge_sort_helper(arr, 0, n - 1)
    return time.time() - start_time, arr

def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    n = len(arr)
    start_time = time.time()
    quick_sort_helper(arr, 0, n - 1)
    return time.time() - start_time, arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return time.time() - start_time, arr

def getNextGap(gap):
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap

def comb_sort(arr):
    n = len(arr)
    gap = n
    start_time = time.time()
    swapped = True
    while gap != 1 or swapped:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    return time.time() - start_time, arr

def cocktail_sort(arr):
    n = len(arr)
    start_time = time.time()
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
    return time.time() - start_time, arr

# Creación de una lista de nombres de algoritmos
algorithm_names = ['BubbleSort', 'InsertSort', 'SelectionSort', 'ShellSort', 'MergeSort', 'QuickSort', 'HeapSort', 'CombSort', 'CocktailSort']

# Creación de una lista de funciones de algoritmos
algorithms = [bubble_sort, insert_sort, selection_sort, shell_sort, merge_sort, quick_sort, heap_sort, comb_sort, cocktail_sort]

class PlotEfficiencyApp(tk.Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.master.title("Comparacion de eficiencia de algoritmos de ordenamiento")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Creación de la etiqueta y entrada para el tamaño máximo del arreglo
        self.max_array_size_label = tk.Label(self, text="Ingrese el tamaño máximo del arreglo:")
        self.max_array_size_label.pack()
        self.max_array_size_entry = tk.Entry(self)
        self.max_array_size_entry.pack()

        # Creación de las casillas de verificación para seleccionar los algoritmos a comparar
        self.algorithm_var_list = []
        for i, algorithm_name in enumerate(algorithm_names):
            var = tk.BooleanVar()
            self.algorithm_var_list.append(var)
            algorithm_checkbutton = tk.Checkbutton(self, text=algorithm_name, variable=var)
            algorithm_checkbutton.pack()

        # Creación del botón para iniciar la comparación de eficiencia
        self.start_button = tk.Button(self, text="Iniciar", command=self.plot_efficiency)
        self.start_button.pack()

    def plot_efficiency(self):
        max_array_size = int(self.max_array_size_entry.get())
        algorithms_to_compare = [algorithms[i] for i, var in enumerate(self.algorithm_var_list) if var.get()]

        algorithm_times = [[] for _ in range(len(algorithms_to_compare))]
        algorithm_times_worst = [[] for _ in range(len(algorithms_to_compare))]
        algorithm_times_best = [[] for _ in range(len(algorithms_to_compare))]
        x_vals = []
        
        for n in range(1, max_array_size+1, 10):
            for i, algorithm_func in enumerate(algorithms_to_compare):
                arr = [random.randint(1, 100000) for _ in range(n)]
                
                # Obtener tiempo para caso promedio
                time_avg, sorted_arr = algorithm_func(arr.copy())
                algorithm_times[i].append(time_avg)
                
                # Obtener tiempo para peor caso (arreglo ordenado en orden descendente)
                arr.sort(reverse=True)
                time_worst, _ = algorithm_func(arr.copy())
                algorithm_times_worst[i].append(time_worst)
                
                # Obtener tiempo para mejor caso (arreglo ordenado en orden ascendente)
                arr.sort()
                time_best, _ = algorithm_func(arr.copy())
                algorithm_times_best[i].append(time_best)
                
            x_vals.append(n)

            # Gráfico de líneas en tiempo real
            plt.clf()
            for i, algorithm_name in enumerate(algorithm_names):
                if algorithms[i] in algorithms_to_compare:
                    plt.plot(x_vals, algorithm_times[algorithms_to_compare.index(algorithms[i])], label=algorithm_name + " (Caso Promedio)")
                    plt.plot(x_vals, algorithm_times_worst[algorithms_to_compare.index(algorithms[i])], label=algorithm_name + " (Peor Caso)", linestyle='dashed')
                    plt.plot(x_vals, algorithm_times_best[algorithms_to_compare.index(algorithms[i])], label=algorithm_name + " (Mejor Caso)", linestyle='dotted')
            plt.legend(loc='upper left')
            plt.title('Comparacion de eficiencia de algoritmos de ordenamiento')
            plt.xlabel('Tamaño del arreglo')
            plt.ylabel('Tiempo de ejecucion (segundos)')
            plt.pause(0.05)

        plt.show()

root = tk.Tk()
app = PlotEfficiencyApp(master=root)
app.mainloop()
