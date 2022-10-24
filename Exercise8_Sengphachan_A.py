Username = input("Enter username: ")
Password = input("Enter password :  ")
if Username == "devil" and Password == "2212":
    print("Loading....")
    print("Welcome to Devil shop")
    print("1. Sun screen lotion : 70USD ")
    print("2. Serum : 60USD ")
    print("3. Sleeping mask : 12USD ")
    print("What do you want?")
    numberOfProduct=int(input("Enter the number of product "))
    if numberOfProduct==1:
        howmany= int(input("How many do you want? "))
        total = howmany*70
        print("Bill :", total,"USD")
    elif numberOfProduct==2:
        howmany= int(input("How many do you want? "))
        total = howmany*60
        print("Bill :", total,"USD")
    elif numberOfProduct==3:
        howmany= int(input("How many do you want? "))
        total = howmany*60
        print("Bill :", total,"USD")
else :
    print("Login fail")
            
        
    