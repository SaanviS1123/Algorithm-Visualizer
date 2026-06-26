class InsertionSort:
    def __init__(self, dataset):
        self.dataset = dataset
        self.steps = []
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.step_count = 0
    
    def execute(self):
        arr = self.dataset.copy()
        
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                self.metrics["comparisons"] += 1
                
                self.steps.append({
                    "step": self.step_count,
                    "array": arr.copy(),
                    "comparing": [j, i],
                    "sorted_indices": list(range(0, i))
                })
                self.step_count += 1
                
                arr[j + 1] = arr[j]
                self.metrics["swaps"] += 1
                j -= 1
            
            arr[j + 1] = key
            self.metrics["swaps"] += 1
            
            self.steps.append({
                "step": self.step_count,
                "array": arr.copy(),
                "comparing": [j + 1, i],
                "sorted_indices": list(range(0, i + 1))
            })
            self.step_count += 1
        
        return self.steps