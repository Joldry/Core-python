# Function to sum all items in a list
def sum_list(items):
    # Initialize the variable to store the sum
    total = 0
    
    # Loop through each item in the list
    for item in items:
        # Add the item to the total sum
        total += item
    
    # Return the total sum
    return total

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Call the sum_list function and print the result
result = sum_list(numbers)
print("The sum of all the items in the list is:", result)



" OUTPUT "

The sum of all the items in the list is: 15
