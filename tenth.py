# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.


#Taking input from the user.
num = int(input("Enter a number: "))

#Passing conditions for checking if the number given is even or odd.
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
