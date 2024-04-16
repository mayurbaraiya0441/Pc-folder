# Ex-7.1
# i) Create a Program that takes a string (a random name). If the last character of the name is an "a", return True, otherwise return False.
# ii) Create a Program that takes a string (a random name). If the last and first character of the name is an "d", return True, otherwise return False.



def checkString(str):
    
 
    # if str[-1]  == 'a':
    #     return True
    # else:
    #     return False
    

    
    
    if str[1]  == 'd' or  str[0] == 'd':
        return True
    else:
        return False

    
    
    
       


# print(checkString('thishasboth29'))
print(checkString('geeksforgeeks'))

