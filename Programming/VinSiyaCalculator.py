#Creating some variables that will store the user input
a = input("Enter first number-")
b = input("Enter second number-")
c = input('''Enter the Operater
+ for addition
- for subtraction
* for multiplication
/ for division-''')
#Typecasting a and b into class interger
a = int(a)
b = int(b)
# telling python that which operator will do which operation
if c == "+":
	print("The answer is",a+b)
elif c == "-":
	print("The answer is",a-b)
elif c == "*":
	print("The answer is",a*b)
elif c == "/":
	print("The answer is",a/b)
else:
	print('''Invalid Operator
Enter a valid operator
examaple-+,-,*,/''')