print()
print("Program starts:")
print()
def optimized_bubble_sort(arr):
    n = len(arr)
    # Flag to check if any swap occurred in the pass
    swapped = False
    
    for i in range(n):
        swapped = False
        # Traverse the list from 0 to n-i-1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, list is sorted – exit early!
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    data = [5, 1, 4, 2, 8]
    optimized_bubble_sort(data)
    print("Optimized sorted array:", data)

print()
print("Program ended.")
print()
