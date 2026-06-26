from src.algorithms.bubble_sort import BubbleSort

data = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSort(data)
steps = sorter.execute()

print(f"Total steps: {len(steps)}")
print(f"Comparisons: {sorter.metrics['comparisons']}")
print(f"Swaps: {sorter.metrics['swaps']}")
print(f"First step: {steps[0]}")