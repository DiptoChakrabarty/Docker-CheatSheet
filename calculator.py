print("Welcome to Inbuilt Calculator\n")
print("Please choose your operation from below options")
while(True):
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    opt = int(input(""" Enter your choice 
                 1) Addition 
                 2) Subtraction 
                 3) Multiply
                 4) Divide
                 press any other number to exit : """))
    
    if(opt==1):
        print("Result is : ",a+b)
    elif(opt==2):
        print("Result is : ",a-b)
    elif(opt==3):
        print("Result is : ",a*b)
    elif(opt==4):
        print("Result is : ",a/b)
    else:
        break