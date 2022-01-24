def my_function(numbers):
    unique_numbres = []
    
    for number in numbers:
        if (number in unique_numbres) != True:
            unique_numbres.append(number)
        
    return unique_numbres

input1=[ 1,  2, 5, 2, 5, 2, 3, 4, 1, 4, 5]
input2=[]
input3=[1,2,3]


remove_duplicity = my_function(input1)
print (remove_duplicity)
remove_duplicity = my_function(input2)
print (remove_duplicity)
remove_duplicity = my_function(input3)
print (remove_duplicity)
