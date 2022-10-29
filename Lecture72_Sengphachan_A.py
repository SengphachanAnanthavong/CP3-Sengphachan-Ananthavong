

menulist= []
def showBill():
    Totalprice = 0
    print("---- Welcome to Gay restaurant ----")
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        Totalprice += int(menulist[number][1])
    
    
       
        
        
        
    print("---- Total ----")
    print(Totalprice)
    

while True:
    menuName = input("Enter menu name : ")
    if menuName.lower() == 'exit':
        
        break
    else :
        menuPrice = input("Enter menu price : ")
        menulist.append([menuName,menuPrice])
        
print(menulist)
showBill()




