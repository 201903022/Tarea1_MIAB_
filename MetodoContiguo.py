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
                    #print("Agregando en ",  (start + i))
                    self.memory[start + i] = True
                return start
        return -1  # No hay bloques contiguos libres de suficiente tamano

    def deallocate(self, start, size):
        """
        Libera un bloque de memoria a partir de una posicion inicial y tamano especificado.
        """
        for i in range(start, start + size):
            self.memory[i] = False

def measure_time(allocator, allocations):
    start_time = time.time()
    print("Inicio: ",allocator.memory)
    for size in allocations:
        print("Size to fill ",size)
        allocator.allocate(size)
    end_time = time.time()
    print("Fin: ",allocator.memory)
    return end_time - start_time

def main():
    total_memory = 1000
    allocations = [100,200,30]

    contiguous_allocator = ContiguousMemoryAllocator(total_memory)
   # print("Memoria: ", contiguous_allocator.memory)

    contiguous_time = measure_time(contiguous_allocator, allocations)
    contiguous_time *= 1000

    print(f"Tiempo de ejecucion (Contiguo): {contiguous_time:.6f} segundos")
    

if __name__ == "__main__":
    main()