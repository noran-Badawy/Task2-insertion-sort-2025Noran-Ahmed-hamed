Problem:

We have a list of names, and we want to sort them alphabetically using the Insertion Sort algorithm instead of sorting numbers.

Solution:

We will use the Insertion Sort algorithm to sort the list, where each element is compared to the previous ones and inserted into the correct position.

Python Code:

def insertion_sort_names(names):
    """
    This function sorts a list of names alphabetically using the Insertion Sort algorithm.
    """
    for i in range(1, len(names)):  # Start from the second element
        key = names[i]  # Current element to be inserted in the correct position
        j = i - 1
        
        # Shift larger elements to the right to make space
        while j >= 0 and names[j].lower() > key.lower():  # Ignore case sensitivity
            names[j + 1] = names[j]
            j -= 1
        
        names[j + 1] = key  # Insert the element in its correct position

# Unsorted list of names
names_list = ["Zain", "ali", "Mona", "Khalid", "sara", "Bilal"]

# Print the list before sorting
print("Before sorting:", names_list)

# Apply the insertion sort algorithm
insertion_sort_names(names_list)

# Print the list after sorting
print("After sorting:", names_list)

Expected Output:

Before sorting: ['Zain', 'ali', 'Mona', 'Khalid', 'sara', 'Bilal']
After sorting: ['ali', 'Bilal', 'Khalid', 'Mona', 'sara', 'Zain']

The list is now sorted alphabetically, with case-insensitive sorting.