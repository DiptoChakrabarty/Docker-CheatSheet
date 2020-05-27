print("Welcome to Inbuilt Calculator\n")
print("Please choose your operation from below options")
while(True):
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    opt = input(""" Enter your choice 
                 1) Addition 
                 2) Subtraction 
                 3) Multiply
                 4) Divide
                 press any other number to exit""")
    
    if(opt==1):
        print(a+b)
    elif(opt==2):
        print(a-b)
    elif(opt==3):
        print(a*b)
    elif(opt==4):
        print(a/b)
    else:
        break