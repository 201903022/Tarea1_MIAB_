class Nodo:
    def __init__(self, tamanio, ocupado=False):
        self.tamanio = tamanio
        self.ocupado = ocupado
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, tamanio):
        nuevo_nodo = Nodo(tamanio)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def encontrar_bloque_libre(self, tamanio):
        actual = self.cabeza
        while actual:
            if not actual.ocupado and actual.tamanio >= tamanio:
                return actual
            actual = actual.siguiente
        return None

    def asignar_bloque(self, tamanio):
        bloque_libre = self.encontrar_bloque_libre(tamanio)
        if bloque_libre:
            bloque_libre.ocupado = True
            return bloque_libre
        else:
            return None

    def liberar_bloque(self, bloque):
        if bloque:
            bloque.ocupado = False


import time
import random

def prueba_asignacion_extensa(lista, num_asignaciones, tamaño_min, tamaño_max):
    print(f"Iniciando prueba de asignación de {num_asignaciones} bloques...")
    inicio = time.time()
    for i in range(num_asignaciones):
        tamaño = random.randint(tamaño_min, tamaño_max)
        bloque = lista.asignar_bloque(tamaño)
        if bloque:
            print(f"Asignación {i+1} de {tamaño} bytes: OK")
        else:
            print(f"Asignación {i+1} de {tamaño} bytes: NO DISPONIBLE")
    fin = time.time()
    print(f"Tiempo total de asignación: {fin - inicio:.6f} segundos")

def prueba_liberacion_extensa(lista, num_liberaciones):
    print(f"Iniciando prueba de liberación de {num_liberaciones} bloques...")
    inicio = time.time()
    for i in range(num_liberaciones):
        bloque = lista.cabeza
        while bloque and bloque.ocupado:
            bloque = bloque.siguiente
        if bloque:
            lista.liberar_bloque(bloque)
            print(f"Liberación {i+1}: OK")
        else:
            print(f"Liberación {i+1}: NO HAY BLOQUES OCUPADOS")
    fin = time.time()
    print(f"Tiempo total de liberación: {fin - inicio:.6f} segundos")

# Crear lista enlazada con 1000 bloques de memoria
lista = ListaEnlazada()
for i in range(1000):
    lista.agregar_nodo(random.randint(100, 10000))

# Pruebas de asignación y liberación extensas
prueba_asignacion_extensa(lista, 500, 1000, 5000)
prueba_liberacion_extensa(lista, 200)
prueba_asignacion_extensa(lista, 300, 500, 2000)
prueba_liberacion_extensa(lista, 150)