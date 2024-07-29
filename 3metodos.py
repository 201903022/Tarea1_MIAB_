import time
#Metodo Contiguo: 
class ContiguousMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [False] * total_memory  # False indica bloque libre
        self.total_memory = total_memory

    def allocate(self, size):
        """
        Asigna un bloque de memoria contiguo del tamano especificado.
        Retorna la posicion inicial del bloque asignado o -1 si no hay espacio suficiente.
        """
        for start in range(self.total_memory - size + 1):
            if all(not self.memory[start + i] for i in range(size)):
                for i in range(size):
                    self.memory[start + i] = True
                return start
        return -1  # No hay bloques contiguos libres de suficiente tamano

    def deallocate(self, start, size):
        """
        Libera un bloque de memoria a partir de una posicion inicial y tamano especificado.
        """
        for i in range(start, start + size):
            self.memory[i] = False

class Node:
    def __init__(self, size, start, free=True):
        self.size = size
        self.start = start
        self.free = free
        self.next = None


#Metodo de lista ligada
class LinkedListMemoryAllocator:
    def __init__(self, total_memory):
        self.head = Node(total_memory, 0)

    def allocate(self, size):
        current = self.head
        while current:
            if current.free and current.size >= size:
                current.free = False
                if current.size > size:
                    new_node = Node(current.size - size, current.start + size)
                    new_node.next = current.next
                    current.next = new_node
                    current.size = size
                return current.start
            current = current.next
        return -1  # No hay bloques libres disponibles

    def deallocate(self, start):
        current = self.head
        while current:
            if current.start == start:
                current.free = True
                break
            current = current.next


#Metodo Indexada: 
class IndexedMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [False] * total_memory  # False indica bloque libre
        self.total_memory = total_memory
        self.index_table = {}  # Tabla de indices para cada proceso

    def allocate(self, process_id, size):
        """
        Asigna bloques de memoria para un proceso dado un tamaño especificado.
        Retorna una lista de indices o -1 si no hay suficientes bloques libres.
        """
        blocks_allocated = 0
        indices = []

        for i in range(self.total_memory):
            if not self.memory[i]:
                self.memory[i] = True
                indices.append(i)
                blocks_allocated += 1
                if blocks_allocated == size:
                    self.index_table[process_id] = indices
                    return indices
        
        # No se encontraron suficientes bloques libres
        for i in indices:
            self.memory[i] = False  # Liberar bloques asignados temporalmente
        return -1

    def deallocate(self, process_id):
        """
        Libera los bloques de memoria asignados a un proceso especifico.
        """
        if process_id in self.index_table:
            for index in self.index_table[process_id]:
                self.memory[index] = False
            del self.index_table[process_id]

def measure_time(allocator, allocations):
    start_time = time.time()
    for size in allocations:
        allocator.allocate(size)
    end_time = time.time()
    return end_time - start_time
def measure_time2(allocator, allocations):
    start_time = time.time()
    for i, size in enumerate(allocations):
        allocator.allocate(i, size)
    end_time = time.time()
    return end_time - start_time

def main():
    total_memory = 100
    allocations = [10, 20, 30, 40, 50,60,70,80,90]

    contiguous_allocator = ContiguousMemoryAllocator(total_memory)
    linked_list_allocator = LinkedListMemoryAllocator(total_memory)
    indexed_allocator = IndexedMemoryAllocator(total_memory)
   

    contiguous_time = measure_time(contiguous_allocator, allocations)
    linked_list_time = measure_time(linked_list_allocator, allocations)
    indexed_time = measure_time2(indexed_allocator, allocations)
    contiguous_time *= 1000
    linked_list_time *= 1000
    indexed_time *= 1000
    print(f"Tiempo de ejecucion (Contiguo): {contiguous_time:.6f} segundos")
    print(f"Tiempo de ejecucion (Lista Enlazada): {linked_list_time:.6f} segundos")
    print(f"Tiempo de ejecucion (Indexado): {indexed_time:.6f} segundos")

if __name__ == "__main__":
    main()
