def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y
print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiple")
print("4.Divide")

choice = input("enter choice(1/2/3/4)")

num1 = int(input("enter a:"))
num2 = int(input("enter b:"))

if choice =='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice =='2':
	print(num1,"-",num2,"=",subtract(num1,num2))
elif choice =='3':
	print(num1,"*",num2,"=",multiple(num1,num2))
elif choice =='4':
	print(num1,"/",num2,"=",divide(num1,num2))
else:
	print("Invaid choice")
