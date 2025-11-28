import heapq
import random
import matplotlib.pyplot as plt
import numpy as np

def visualize_step(step, heap, current_min, merged, chunk_data, title):
    """Visualization of the current state of the algorithm"""
    plt.figure(figsize=(12, 8))
    
    
    plt.subplot(2, 2, 1)
    if heap:
        heap_values = [x[0] for x in heap]
        plt.bar(range(len(heap_values)), heap_values, color='lightblue')
        plt.title('(min-heap)')
        plt.xlabel('index-heap')
        plt.ylabel('value')
        for i, v in enumerate(heap_values):
            plt.text(i, v, str(v), ha='center', va='bottom')
    
   
    plt.subplot(2, 2, 2)
    if merged:
        plt.plot(merged, 'go-', markersize=8, linewidth=2)
        plt.title('sorted resut')
        plt.xlabel('position')
        plt.ylabel('value')
        for i, v in enumerate(merged):
            plt.text(i, v, str(v), ha='center', va='bottom')
    
    
    plt.subplot(2, 2, 3)
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
    for i, chunk in enumerate(chunk_data):
        if chunk:
            x_pos = [i * 10 + j for j in range(len(chunk))]
            plt.scatter(x_pos, chunk, color=colors[i % len(colors)], s=100, label=f'chunk {i}')
            for j, val in enumerate(chunk):
                plt.text(x_pos[j], val, str(val), ha='center', va='bottom')
    plt.title('current data in chunk')
    plt.xlabel('position in chunk')
    plt.ylabel('value')
    plt.legend()
    
   
    plt.subplot(2, 2, 4)
    if current_min is not None:
        plt.text(0.5, 0.5, f'current min: {current_min}', 
                fontsize=20, ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgreen'))
        plt.title('extracted element')
    plt.axis('off')
    
    plt.suptitle(f'{title} (step: {step})', fontsize=16)
    plt.tight_layout()
    plt.show()

def simple_external_sort():
    """Simplified external sorting with visualization"""
    
    
    print("generation of data")
    data = [random.randint(1, 50) for _ in range(20)]
    print(f"generated: {data}")
    
    
    print("\n phase 1: sorting chunks")
    chunk_size = 5
    chunks = []
    
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        print(f"chunk {len(chunks)} before: {chunk}")
        chunk.sort()
        print(f"chunk {len(chunks)} after: {chunk}")
        chunks.append(chunk)
    
    
    print("\n🔄 phase 2: merge")
    
    
    iterators = [iter(chunk) for chunk in chunks]
    heap = []
    merged = []
    
    
    print("🔹 initializing cheap:")
    for i, it in enumerate(iterators):
        try:
            val = next(it)
            heapq.heappush(heap, (val, i))
            print(f"  added: {val} from chunk {i}")
        except StopIteration:
            pass
    
    step = 0
    print(f"\n starting merge")
    print(f"heap: {[x[0] for x in heap]}")
    
    while heap:
        step += 1
        
        
        current_chunks = []
        for i, it in enumerate(iterators):
            chunk_vals = list(chunks[i]) if i < len(chunks) else []
            current_chunks.append(chunk_vals)
        
        
        value, chunk_idx = heapq.heappop(heap)
        merged.append(value)
        
        print(f"\n step {step}:")
        print(f"   extracted: {value} (from chunk {chunk_idx})")
        print(f"   result: {merged}")
        
        
        visualize_step(step, heap, value, merged, current_chunks, "outsort")
        
       
        try:
            next_val = next(iterators[chunk_idx])
            heapq.heappush(heap, (next_val, chunk_idx))
            print(f"   added: {next_val} (from chunk {chunk_idx})")
        except StopIteration:
            print(f"   chunk {chunk_idx} ended")
        
        print(f"   heap: {[x[0] for x in heap]}")
    
    
    print("\n result:")
    print(f"initial data: {data}")
    print(f"sorted: {merged}")
    print(f"accuracy: {merged == sorted(data)}")
    
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.bar(range(len(data)), data, color='red', alpha=0.7)
    plt.title('initial data')
    plt.xlabel('idx')
    plt.ylabel('value')
    
    plt.subplot(1, 2, 2)
    plt.bar(range(len(merged)), merged, color='green', alpha=0.7)
    plt.title('sorted data')
    plt.xlabel('idx')
    plt.ylabel('value')
    
    for i, v in enumerate(merged):
        plt.text(i, v, str(v), ha='center', va='bottom')
    
    plt.suptitle('final result', fontsize=16)
    plt.tight_layout()
    plt.show()

def ultra_simple_version():
    """only console"""
    print("only console visual")
    print("=" * 40)
    
    
    data = [random.randint(1, 30) for _ in range(12)]
    chunk_size = 4
    
    print(f"data: {data}")
    print(f"chunk size: {chunk_size}")
    
    
    print("\n sorting chunks:")
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        chunk.sort()
        chunks.append(chunk)
        print(f"chunk {len(chunks)-1}: {chunk}")
    
    
    print("\n merge:")
    heap = []
    merged = []
    
    
    for i, chunk in enumerate(chunks):
        if chunk:
            heapq.heappush(heap, (chunk[0], i, 0))
    
    step = 0
    while heap:
        step += 1
        val, chunk_idx, elem_idx = heapq.heappop(heap)
        merged.append(val)
        
        print(f"step {step}: extracted {val} from chunk {chunk_idx}")
        print(f"result: {merged}")
        
        
        if elem_idx + 1 < len(chunks[chunk_idx]):
            next_val = chunks[chunk_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, chunk_idx, elem_idx + 1))
    
    print(f"\n final result: {merged}")
    print(f"accuracy of sorting: {merged == sorted(data)}")


if __name__ == "__main__":
    print("Choose:")
    print("1. full version with visual")
    print("2. simple version (only console)")
    
    choice = input("input 1 or 2: ").strip()
    
    if choice == "1":
        simple_external_sort()
    else:
        ultra_simple_version()