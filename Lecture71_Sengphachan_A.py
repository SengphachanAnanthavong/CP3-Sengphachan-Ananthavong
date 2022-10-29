
TotalPrice = 0
menuList= []
priceList = []
def showBill():
    print("---- Welcome to Gay restaurant ----")
    
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        
        
        
    print("---- Total ----")
    print(TotalPrice)

while True:
    menuName = input("Enter menu name : ")
    if menuName.lower() == 'exit':
        
        break
    else :
        menuPrice = input("Enter menu price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
        TotalPrice += int(menuPrice)
showBill()



