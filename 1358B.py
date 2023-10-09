def create_unique_set(arr):
    unique_set = set()
    
    for item in arr:
        if item not in unique_set:
            unique_set.add(item)
    
    return unique_set

# Example array
input_array = [2,3,2,4,1,3,4,1]

unique_values_set = create_unique_set(input_array)
print(unique_values_set)
