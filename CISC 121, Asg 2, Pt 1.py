'''
CISC-121 2022F

Name: Yun Kyaw
Date: 2022-10-05

I confirm that this assignment solution is my own work and conforms to
Queen’s standards of Academic Integrity
'''

def get_input():
    """
    This function gets the input and makes sure it is valid
    Input:
        none
    Output:
        values - list of int
        
    """
    valid = False
    
    while valid == False:   # the inputting process will loop until both values are valid
        integer_input = input("Please enter two numbers between -20 and 20 separated by a space: ")
        
        values = integer_input.split(" ")  # splitting the input to have 2 values
        
        values[0] = int(values[0])
        
        values[1] = int(values[1])
        
        # this section checks if the values are valid
        if values[0] > -20 and values[0] < 20:
            value_one = True
        else:
            value_one = False
            
        if values[1] > -20 and values[1] < 20:  #
            value_two = True
        else:
            value_two = False
        
        # this section tells the user is their inputs are or arent valid, it also ends the loop if both values are valid
        if value_one == True and value_two == True:
            print("Both numbers are valid")
            valid = True
        elif value_one == True:
            print("The second number (", values[1],") is invalid", sep = "")
        elif value_two == True:
            print("The first number (", values[0],") is invalid", sep = "")
        else:
            print("Both numbers", values, "are invalid")

    return(values)


def dividing_values(values):
    """
    This function prints the numbers in the range of the given values that are divisible by five and prints the answer
    Input:
        value_one: int
        value_two: int
    Output:
        ans: int
    """
    value_one = values[0]
    value_two = values[1]
    
    if value_one >= value_two:
        for i in range(value_one, value_two, -5):
            if i == value_one:  # here, the first value is skipped
                pass
            else: 
                ans = i // 5
                ans *= 5
                print(ans)
    else:
        for i in range(value_one, value_two, 5):
            if i == value_one:  # here, the first value is skipped
                pass
            else: 
                ans = i // 5
                ans *= 5
                print(ans)


def main():
    loop = True
    
    while loop == True:
        int_values = get_input() 
        dividing_values(int_values)
        
        loop_input = input("Would you like to run this again (Yes or No)? ")
        if loop_input == "No" or loop_input == "no":
            loop = False
        else:
            continue
        
    print("... exiting...")
    
main()

    