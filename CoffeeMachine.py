from replit import clear
from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 0,
    "milk": 0,
    "coffee": 800,
}
profit = 0

#Check if the resource is sufficient
def resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients: #loop through the ingredients dictionary to get a hold for each "item"
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item.upper()} \n")
            is_enough = False
    return is_enough  #i.e is_enough = True


def process_coins():
    '''Returns total calculated froms coins inserted'''
    print("Please Insert Coins... \n")
    total = int(input(" How many Quarters: "))*0.25  #multiply to change the input to currency type
    total += int(input("How many Dimes: "))*0.10
    total += int(input("How many Nickles: "))*0.05
    total += int(input("How many Pennies: "))*0.01
    return total

#Check if payment is successful
def transaction_successful(moneyRecieved, drinkCost):
    """returns true if payment accepted or else False"""
    if moneyRecieved >= drinkCost:
        change = round(moneyRecieved - drinkCost, 2) #return change if exceess money inserted
        print(f"Here's Your Change- ${change}")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry money not enough. Money refunded")
        return False


#deduct the amount of ingredients of the user's drink from resources if sufficient resources and transaction is successful
def makeCoffee(drinkName, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Heres Your {drinkName.upper()}. Enjoy \n \n")




#machine running/restarting function
def run():
    Main_switch = True #True = On
    password = 543210

    while Main_switch == True:
        print(logo)
        print("\n \n")
        choice = input("What would you like? (espresso / latte / cappuccino) \t").lower()
        if choice == "off":
            if int(input("Enter Password For Master control: ")) == password:
                print("Shutting Down!! ")
                Main_switch = False
            else:
                print("Wrong Password")               
        elif choice == "restart": #To restart system after master control
            if int(input("Enter Password For Master control: ")) == password:
                clear()
                run()           
        elif choice == "report":
            if int(input("Enter Password For Master control: ")) == password:
                print(f"water: {resources['water']}ml")
                print(f"milk: {resources['milk']}ml")
                print(f"coffee: {resources['coffee']}g")
                print(f"money: {profit}")
        else:
            drink = MENU[choice] #Drink according to user choice
            # print(drink)
            if resource_sufficient(drink["ingredients"]): #"ingredients" dictionary inside the order keyword say "latte" is passed as arguement in the resource_sufficient() functn
                payment = process_coins()
                if transaction_successful(payment, drink["cost"]): 
                    makeCoffee(choice, drink["ingredients"])

clear()
run()