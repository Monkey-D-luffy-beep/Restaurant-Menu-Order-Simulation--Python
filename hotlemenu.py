#Define the menu of Restaurant
menu = {
    'Pizza' :480,
    'Pasta' :500,
    'Burger':260,
    'Coffee': 320,
    
}

#Greeting
print("Welcome to Aeroline")
print("Pizza   :480 Rs\nPasta   :500 Rs\nBurger  :260 Rs\nCoffee  :320 Rs\n")

Order_Total = 0

item_1 = input("Enter the name of item you want to order?")
if item_1 in menu:
    Order_Total += menu[item_1]   
    print(f"YOur item {item_1} has been added to your Order")

else:
    print(f"Order Item{item_1} is not available yet")

another_order = input("Do you want anything else from the menu?  (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of the Second item")
    if item_2 in menu:
        Order_Total +=menu[item_2]
        print(f"Item {item_2} has been added to your Order")
    else:
        print(f"Order Item {item_2} is not available!")
print(f" Here is Bill {Order_Total} Rs Hope you Enjoyed your Imaginary Food :)")