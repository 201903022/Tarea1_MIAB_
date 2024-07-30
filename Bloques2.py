import time

class BitVectorMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [0] * total_memory  # 0 indica bloque libre
        self.total_memory = total_memory
        self.free_blocks = {i: i for i in range(total_memory)}  # Mapa de bloques libres

    def allocate(self, size):
        start = self.find_free_block(size)
        if start != -1:
            for i in range(start, start + size):
                self.memory[i] = 1  # Marcar como ocupado
                del self.free_blocks[i]  # Eliminar del mapa de bloques libres
            return start
        return -1  # No hay bloques libres de suficiente tamano

    def deallocate(self, start, size):
        for i in range(start, start + size):
            self.memory[i] = 0  # Marcar como libre
            self.free_blocks[i] = i  # Añadir al mapa de bloques libres

    def find_free_block(self, size):
        free_count = 0
        start = -1
        for i in range(self.total_memory):
            if self.memory[i] == 0:
                free_count += 1
                if free_count == size:
                    start = i - size + 1
                    break
            else:
                free_count = 0
        return start

def measure_time(allocator, allocations):
    start_time = time.time()
    print("Inicio")
    print(allocator.memory)
    for size in allocations:
        allocator.allocate(size)
    end_time = time.time()
    print()
    print(allocator.memory)
    return end_time - start_time

def main():
    total_time = 0
    for _ in range(5):
        total_memory = 1000
        allocations = [20, 30, 60, 80]

        bit_vector_allocator = BitVectorMemoryAllocator(total_memory)

        bit_vector_time = measure_time(bit_vector_allocator, allocations)
        bit_vector_time *= 10000  # Escalar para comparación
        total_time += bit_vector_time
        print(f"Tiempo de ejecución (Vector de Bits): {bit_vector_time:.6f} segundos")
    print(f"Tiempo promedio (Vector de Bits): {total_time / 5:.6f} segundos")

if __name__ == "__main__":
    main()
