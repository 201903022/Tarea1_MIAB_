import time

# Clases de los metodos Contiguo y Lista Enlazada van aqui

class IndexedMemoryAllocator:
    def __init__(self, total_memory):
        self.memory = [False] * total_memory
        self.total_memory = total_memory
        self.index_table = {}

    def allocate(self, process_id, size):
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
        for i in indices:
            self.memory[i] = False
        return -1

    def deallocate(self, process_id):
        if process_id in self.index_table:
            for index in self.index_table[process_id]:
                self.memory[index] = False
            del self.index_table[process_id]

def measure_time(allocator, allocations):
    start_time = time.time()
    print("Inicio: ",allocator.memory)
    for i, size in enumerate(allocations):
        allocator.allocate(i, size)
    end_time = time.time()
    print("Fin: ",allocator.memory)
    return end_time - start_time

def main():
    total_memory = 100
    allocations = [10, 20, 30, 40, 50]

    #contiguous_allocator = ContiguousMemoryAllocator(total_memory)
    #linked_list_allocator = LinkedListMemoryAllocator(total_memory)
    indexed_allocator = IndexedMemoryAllocator(total_memory)

   # contiguous_time = measure_time(contiguous_allocator, allocations)
    #linked_list_time = measure_time(linked_list_allocator, allocations)
    indexed_time = measure_time(indexed_allocator, allocations)

    indexed_time *= 10000
    #print(f"Tiempo de ejecucion (Contiguo): {contiguous_time:.6f} segundos")
    #print(f"Tiempo de ejecucion (Lista Enlazada): {linked_list_time:.6f} segundos")
    print(f"Tiempo de ejecucion (Indexado): {indexed_time:.6f} segundos")

if __name__ == "__main__":
    main()
