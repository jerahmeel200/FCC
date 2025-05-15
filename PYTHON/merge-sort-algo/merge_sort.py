def merge_sort(array):  # Define the merge_sort function that takes an array as input
    if len(array) <= 1:  # Base case: if the array has 1 or no elements, it's already sorted
        return  # Exit the function
    
    middle_point = len(array) // 2  # Find the middle index of the array
    left_part = array[:middle_point]  # Split the array into the left half
    right_part = array[middle_point:]  # Split the array into the right half

    merge_sort(left_part)  # Recursively sort the left half
    merge_sort(right_part)  # Recursively sort the right half

    left_array_index = 0  # Initialize index for the left half
    right_array_index = 0  # Initialize index for the right half
    sorted_index = 0  # Initialize index for the merged array

    # Merge the two halves into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):  # While both halves have elements
        if left_part[left_array_index] < right_part[right_array_index]:  # Compare elements from both halves
            array[sorted_index] = left_part[left_array_index]  # Place the smaller element into the array
            left_array_index += 1  # Move to the next element in the left half
        else:
            array[sorted_index] = right_part[right_array_index]  # Place the smaller element into the array
            right_array_index += 1  # Move to the next element in the right half
        sorted_index += 1  # Move to the next position in the merged array

    # Copy any remaining elements from the left half
    while left_array_index < len(left_part):  # If there are elements left in the left half
        array[sorted_index] = left_part[left_array_index]  # Add them to the array
        left_array_index += 1  # Move to the next element in the left half
        sorted_index += 1  # Move to the next position in the merged array
    
    # Copy any remaining elements from the right half
    while right_array_index < len(right_part):  # If there are elements left in the right half
        array[sorted_index] = right_part[right_array_index]  # Add them to the array
        right_array_index += 1  # Move to the next element in the right half
        sorted_index += 1  # Move to the next position in the merged array


if __name__ == '__main__':  # Entry point of the program
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]  # Define an unsorted array
    print('Unsorted array: ')  # Print a message
    print(numbers)  # Print the unsorted array
    merge_sort(numbers)  # Call the merge_sort function to sort the array
    print('Sorted array: ' + str(numbers))  # Print the sorted array