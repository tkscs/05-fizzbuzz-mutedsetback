#variable representing your maximum number

#make a for loop that goes from 1 to your max number (including your max number)

#print each number UNLESS the number is a multiple of 3 or 5

#if the number is a multiple of 3 and not 5, print "fizz" instead of the number

#f the number is a multiple of 5 and not 3, print "buzz" instead of the number

#if the number is a multiple of both 3 and 5, print "fizzbuzz" instead of the number



max_number = 15

#start

for x in range(1, max_number + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

