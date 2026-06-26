class BubbleSort:
    def __init__(self, dataset):
        self.dataset=dataset
        self.steps=[]
        self.metrics={"comparisons":0, "swaps":0}
    
    def execute(self):
            arr = self.dataset.copy()  
            step_count = 0
            for i in range(len(arr)):
                for j in range(len(arr) - i - 1):  
                    self.metrics["comparisons"] += 1
                    
                    self.steps.append({
                        "step": step_count,
                        "array": arr.copy(),
                        "comparing": [j, j + 1],
                        "sorted_indices": list(range(len(arr) - i, len(arr)))
                    })
                    step_count += 1
                    
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        self.metrics["swaps"] += 1
            
            return self.steps
                        





