import time

class BitVectorMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [0] * total_memory  # 0 indica bloque libre
        self.total_memory = total_memory
        self.memory[5] = 1
    def allocate(self, size):
        for start in range(self.total_memory - size + 1):
            if all(self.memory[start + i] == 0 for i in range(size)):
                for i in range(size):
                    self.memory[start + i] = 1  # Marcar como ocupado
                return start
        return -1  # No hay bloques libres de suficiente tamano

    def deallocate(self, start, size):
        for i in range(start, start + size):
            self.memory[i] = 0  # Marcar como libre

def measure_time(allocator, allocations):
    start_time = time.time()
    print("inicio")
    print(allocator.memory)
    for size in allocations:
        allocator.allocate(size)
    end_time = time.time()
    print("final 1")
    print(allocator.memory)
    allocator.deallocate(10,10)
    print("delocate")
    print(allocator.memory)
    
    allocator.allocate(8)
    print("final 2")
    print(allocator.memory)
    return end_time - start_time

def main():
    time = 0
    for _ in range(1): 
        #print("hola")
        total_memory = 1000
        allocations = [20,30,60,80]

        bit_vector_allocator = BitVectorMemoryAllocator(total_memory)

        bit_vector_time = measure_time(bit_vector_allocator, allocations)
        bit_vector_time *= 10000
        time += bit_vector_time
        print(f"Tiempo de ejecucion (Vector de Bits): {bit_vector_time:.6f} segundos")
    print(f"Tiempo promedio (Vector de Bits): {time/5:.6f} segundos")

if __name__ == "__main__":
    main()
