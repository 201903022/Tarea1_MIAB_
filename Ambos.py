import time

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

def measure_time(allocator, allocations):
    start_time = time.time()
    for size in allocations:
        allocator.allocate(size)
    end_time = time.time()
    return end_time - start_time

def main():
    total_memory = 100
    allocations = [10, 20, 30, 40, 50,60,70]

    contiguous_allocator = ContiguousMemoryAllocator(total_memory)
    linked_list_allocator = LinkedListMemoryAllocator(total_memory)

    contiguous_time = measure_time(contiguous_allocator, allocations)
    linked_list_time = measure_time(linked_list_allocator, allocations)

    print(f"Tiempo de ejecucion (Contiguo): {contiguous_time:.6f} segundos")
    print(f"Tiempo de ejecucion (Lista Enlazada): {linked_list_time:.6f} segundos")

if __name__ == "__main__":
    main()
