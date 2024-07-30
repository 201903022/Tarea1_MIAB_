import time

globalTime = 0
class ContiguousMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [False] * total_memory  # False indica bloque libre
        self.total_memory = total_memory
        self.memory[5] = True

    def allocate(self, size):
        for start in range(self.total_memory - size + 1):
            if all(not self.memory[start + i] for i in range(size)):
                for i in range(size):
                    #print("Agregando en ",  (start + i))
                    self.memory[start + i] = True
                return start
        return -1  

    def deallocate(self, start, size):
        for i in range(start, start + size):
            self.memory[i] = False

def measure_time(allocator, allocations):
    print("Inicio: ")
    print(allocator.memory)
    start_time = time.time()
    for size in allocations:
        #print("Size to fill ",size)
        allocator.allocate(size)
    end_time = time.time()
    print("Fin: ")
    print(allocator.memory)
    return end_time - start_time

def main():
    global globalTime
    for i in range(5): 
        total_memory = 1000
        allocations = [3,2,300,500,5]

        contiguous_allocator = ContiguousMemoryAllocator(total_memory)
       # print("Memoria: ", contiguous_allocator.memory)

        contiguous_time = measure_time(contiguous_allocator, allocations)
        contiguous_time *= 1000
        globalTime += contiguous_time

        print(f"Tiempo de ejecucion (Contiguo): {contiguous_time:.6f} segundos")        

    print(f"Tiempo promedio (Contiguo): {globalTime/5:.6f} segundos")        
if __name__ == "__main__":
    main()