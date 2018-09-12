#this function returns the value of the factorial of the entered integer.
#Note - If a negative integer is entered, the return value is a string type.
def factorial(x) :
  if x == 0 :
    return 1
  if x < 0:
    return " not defined! Factorials are only defined for whole numbers, please try again."
  return x*factorial(x-1)
print ("Hello User")
y = int(input("Enter the number whose factorial is to be calculated : "))
print('The required answer is :' , factorial(y)
