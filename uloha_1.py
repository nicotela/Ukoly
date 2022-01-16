def my_function(numbers):
    even = []
    odd = []
    for number in numbers:
        if (number % 2) == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd

input1 = []
input2 = [1,3,5,35,55,72]
input3 = [0,2,5,8,23]

sude, liche = my_function(input1)
print (sude, liche)
sude, liche = my_function(input2)
print (sude, liche)
sude, liche = my_function(input3)
print (sude, liche)
 
