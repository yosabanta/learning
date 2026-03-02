#defining a function as factorial
def factorial(a):  #'a' is the argument
    if a == 0:
        return 1 #as factorial of 0 is 1
    else:
        return a * factorial(a-1) #recursion(the function is again calling itself until the condition is satisfied
#taking input from the user
num = int(input("Enter a number: "))
#calling the function
factorial(num)
#Final result
print(f'Factorial of {num} is {factorial(num)}.')