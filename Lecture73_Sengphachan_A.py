systemMenu = {"Chicken": 35, "fish": 45, "Dog": 55, "cat": 20}
menuList = []
total = 0

def showBill():
    
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
    print("---- Total ----")
    print(total)
    

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
        total += systemMenu[menuName]

showBill()    