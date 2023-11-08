# string-or-integers.py
#the 1st way of doing that:
def filter_integers(mixed_list):
    integers_only = [item for item in mixed_list if isinstance(item, int)]
    strings_only = [item for item in mixed_list if isinstance(item, str)]
    return integers_only

print(filter_integers([1, 'apple', 8, 'banana', 3]))  # Выведет: [1, 2, 3]


# the 2nd way, where the program will sort the lists based on if it is an int or str
def sort_input(strings_list, integers_list):
    user_input = input("Enter an element to sort into the lists: ")

    try:
        int_input = int(user_input)
        integers_list.append(int_input)
    except ValueError:
        #If conversion fails (ValueError is raised), input is a string, append to strings_list
        strings_list.append(user_input)
      
    return strings_list, integers_list


strings = []
integers = []

# Call the function
strings, integers = sort_input(strings, integers)

print("Strings List:", strings)
print("Integers List:", integers)
