# Ex-3.4
# Write a function/program that takes a list of numbers and returns a list with two elements:
# 	The first element should be the sum of all even numbers in the list.
# 	The second element should be the sum of all odd numbers in the list.



def myfunction():
    
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    even_list=[]
    odd_list=[]
    
    print(x)
    for i in x:
        # print(i)
        
        if (i % 2) == 0:
            print("even",i)
            even=i
            even_list.append(even)
                

        else:
            print("odd",i)  
            odd=i
            odd_list.append(odd)
            
            
            
    print(even_list,'even_list')
    print(odd_list,'odd_list')
    
    # sum_even = sum(even)
    print(sum(even))
 
    # sum_odd = sum(odd)
    print(sum(odd))
        
    
 



# sum_even=myfunction()
# print(sum_even)
myfunction()
    
    

    
    

