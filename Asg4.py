'''
CISC-121 2022F

Date: 2022-11-24

I confirm that this assignment solution is my own work and conforms to
Queen’s standards of Academic Integrity
'''
## Question 1
def check_string(user_str):
    """
    This function removes non-alphabetic characters, and checks that the user input is valid, and if not, prompts for a valid input
    Parameters
    - user_str: str
    Returns
    - user_str: str
    """
    new_str = ""
    for letter in user_str:
        if letter.isalpha() == True:  # this adds alphabetic characters to the new string
            new_str += letter
                
    if len(new_str) <= 10:
        return new_str.upper()
    else:  # if this new string has >10 characters, only the first 10 will be used
        return new_str[:10].upper()


def quicksort_list(user_str):
    """
    This function sorts the string alphabetically using quick sort
    Parameters
    - user_str : str
    Returns
    - quicksort_list(less) + equal + quicksort_list(greater): list
    """
    if len(user_str) <= 1:  # if the string is 1 or 0 characters, it doesnt need to be sorted
        return user_str
    else:
        pivot = user_str[(len(user_str)-1)//2]
        less, equal, greater = [], [], []
        for letter in user_str:
            if letter < pivot:  # if the character is before the pivot in the alphabet, it is added to the front of the list 
                less.append(letter)
            elif letter > pivot:  # if the character is after the pivot in the alphabet, it is added to the end of the list 
                greater.append(letter)
            else:
                equal.append(letter)
    return quicksort_list(less) + equal + quicksort_list(greater)


def quicksort_str(sorted_list):
    """
    This function turns the list from the quicksort function into a string
    Parameters
    - sorted_list : list
    Returns
    - sorted_str: str
    """
    sorted_str = ""
    for item in sorted_list:
        sorted_str += item
    return sorted_str


def main_Q1():
    user_str = input("Please enter a string letters: ")
    user_str = check_string(user_str)
    print("The user string is:", user_str)
    
    sorted_list = quicksort_list(user_str)
    sorted_str = quicksort_str(sorted_list)
    print("The sorted string is:", sorted_str)
    return sorted_str
 


## Question 2
def remove_duplicates(sorted_str):
    """
    This function removes duplicates from the string
    Parameters
    - sorted_str: str
    Returns
    - new_str: str
    """
    new_str = ""
    for letter in sorted_str:
        if letter not in new_str:
            new_str += letter
    return new_str


def str_permutation(new_str):
    """
    This function finds all permutations of the string
    Parameters
    - new_str: str
    Returns
    - perm_list: list of str
    """
    if len(new_str) == 1:  # if the string is only one character, it only has one permutation
        return new_str

    perm_list = []
    
    for perm in str_permutation(new_str[1:]):  # for each letter in the string, it creates a permutation 
        for i in range(len(new_str)):  # for each letter, it goes through the string to create a permutation for this letter
            perm_list.append(perm[:i] + new_str[0:1] + perm[i:])
    return perm_list


def main_Q2():
    sorted_str = main_Q1()
    new_str = remove_duplicates(sorted_str)
    perm_list = str_permutation(new_str)
    print("The permutations of this string:", perm_list, sep = "\n")

main_Q2()
    