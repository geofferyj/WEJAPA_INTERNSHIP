#Nearest Square
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40
i = 0

# write your while loop here
while True:
    
    if i**2 > limit:
        break
    
    nearest_square = i**2
    i +=1

print(nearest_square)