'''
CISC-121 2022F

Name: Yun Kyaw
Date: 2022-10-05

I confirm that this assignment solution is my own work and conforms to
Queen’s standards of Academic Integrity
'''

def creating_list(file):
    """
    This function creates a 2D list from the data
    Input:
        data - text file/list
    Output:
        file_list - 2d list
    """
    data = file.read().split("\n")  # reading the file and turning every new line into an item in the list
    
    file_list = []

    for i in range(len(data)):
        line = data[i].split("\t")  # splitting each line in the list to two values
        file_list.append(line)
    
    return(file_list)
    
  
def count_friends(data):
    """
    This function determines how many friends each person has by creating a dictrionary with each person as the key,
    and their amount of friends as the value
    Input:
        data - 2D list
    Output:
        friend_count - dictionary
    """
    friend_count = {}

    for i in range(len(data)):
        for name in data[i]:
            if name in friend_count:  # if this person is in the dictionary, they will have a friend added to their count
                friend_count[name] += 1
            else: 
                friend_count[name] = 1  #if this person isnt in the dictionary, they will be and it will include this friendship
    
    return(friend_count)


def main(file):
    data = open(file, "r")  # opening the file, allowing for this file to be exchanged with another
    
    file_list = creating_list(data)
    
    friend_count = count_friends(file_list)
    
    for key in friend_count:
        print(key, "has", friend_count[key], "friends")
        
main("friendship.txt")
