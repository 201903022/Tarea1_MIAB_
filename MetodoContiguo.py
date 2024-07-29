class ContiguousMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [False] * total_memory  # False indica bloque libre
        self.total_memory = total_memory

    def allocate(self, size):
        """
        Asigna un bloque de memoria contiguo del tamaño especificado.
        Retorna la posición inicial del bloque asignado o -1 si no hay espacio suficiente.
        """
        for start in range(self.total_memory - size + 1):
            if all(not self.memory[start + i] for i in range(size)):
                for i in range(size):
                    self.memory[start + i] = True
                return start
        return -1  # No hay bloques contiguos libres de suficiente tamaño

    def deallocate(self, start, size):
        """
        Libera un bloque de memoria a partir de una posición inicial y tamaño especificado.
        """
        for i in range(start, start + size):
            self.memory[i] = False

# Ejemplo de uso
allocator = ContiguousMemoryAllocator(100)
print("Bloque asignado en indice:", allocator.allocate(10))  # Debería retornar 0
print("Bloque asignado en indice:", allocator.allocate(20))  # Debería retornar 10
print("Estado de la memoria:", allocator.memory)
allocator.deallocate(0, 10)  # Liberar el bloque de 10 en la posición 0
print("Estado de la memoria despues de liberar:", allocator.memory)
