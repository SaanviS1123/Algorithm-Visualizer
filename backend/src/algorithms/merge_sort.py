class MergeSort:
    def __init__(self, dataset):
        self.dataset = dataset
        self.steps = []
        self.metrics = {"comparisons": 0, "swaps": 0}
        self.step_count = 0
    
    def execute(self):
        arr = self.dataset.copy()
        self._merge_sort_helper(arr, 0, len(arr) - 1)
        return self.steps
    
    def _merge_sort_helper(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_helper(arr, left, mid)
            self._merge_sort_helper(arr, mid + 1, right)
            self._merge(arr, left, mid, right)
    
    def _merge(self, arr, left, mid, right):
        left_arr = arr[left:mid + 1].copy()
        right_arr = arr[mid + 1:right + 1].copy()
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            self.metrics["comparisons"] += 1
            
            # Capture which elements are being compared
            self.steps.append({
                "step": self.step_count,
                "array": arr.copy(),
                "comparing": [left + i, mid + 1 + j],
                "sorted_indices": []
            })
            self.step_count += 1
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                self.metrics["swaps"] += 1
                
                # Show the swap
                self.steps.append({
                    "step": self.step_count,
                    "array": arr.copy(),
                    "comparing": [left + i, k],
                    "sorted_indices": []
                })
                self.step_count += 1
                
                i += 1
            else:
                arr[k] = right_arr[j]
                self.metrics["swaps"] += 1
                
                # Show the swap
                self.steps.append({
                    "step": self.step_count,
                    "array": arr.copy(),
                    "comparing": [mid + 1 + j, k],
                    "sorted_indices": []
                })
                self.step_count += 1
                
                j += 1
            
            k += 1
        
        # Handle remaining elements
        while i < len(left_arr):
            arr[k] = left_arr[i]
            self.metrics["swaps"] += 1
            self.steps.append({
                "step": self.step_count,
                "array": arr.copy(),
                "comparing": [left + i, k],
                "sorted_indices": []
            })
            self.step_count += 1
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            self.metrics["swaps"] += 1
            self.steps.append({
                "step": self.step_count,
                "array": arr.copy(),
                "comparing": [mid + 1 + j, k],
                "sorted_indices": []
            })
            self.step_count += 1
            j += 1
            k += 1