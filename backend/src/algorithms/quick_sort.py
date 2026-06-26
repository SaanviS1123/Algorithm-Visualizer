class QuickSort:
    def __init__(self, dataset):
        self.dataset = dataset
        self.steps = []
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.step_count = 0
    
    def execute(self):
        arr = self.dataset.copy()
        self._quicksort_helper(arr, 0, len(arr) - 1)
        return self.steps
    
    def _quicksort_helper(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quicksort_helper(arr, low, pivot_index - 1)
            self._quicksort_helper(arr, pivot_index + 1, high)
    
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            self.metrics["comparisons"] += 1
            
            # Capture snapshot
            self.steps.append({
                "step": self.step_count,
                "array": arr.copy(),
                "comparing": [i + 1, j],
                "sorted_indices": []
            })
            self.step_count += 1
            
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.metrics["swaps"] += 1
        
        # Move pivot to correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.metrics["swaps"] += 1
        
        # Capture final position
        self.steps.append({
            "step": self.step_count,
            "array": arr.copy(),
            "comparing": [i + 1, high],
            "sorted_indices": []
        })
        self.step_count += 1
        
        return i + 1