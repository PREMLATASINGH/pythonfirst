a=float(input("Enter a number: "))
if a>0:
    print("The number is positive.")
elif a<0:
    print("The number is negative.")
else:
    print("The number is zero.")

b=int(input("Enter a number: "))
if b>=18:
    print("You are an adult.")
else:    print("You are a minor.") 
age=12
if age<13:
    print("You are a child.")
elif age<20:
    print("You are a teenager.")
else:
    print("You are an adult.")

x=int(input("Enter a number: "))
if x>=0:
    print("The number is non-negative.")
    if x%2==0:
        print("The number is even.")    
    else:        print("The number is odd.")
else:    print("The number is negative.")
