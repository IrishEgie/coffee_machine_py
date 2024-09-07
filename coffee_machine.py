import menu as m
import art
#initialize global variables here
menu = m.menu #is dictionary
res = m.resources  #is dictionary
logo = art.logo #is multiline string
thanks = art.fin
power = True #is bool

def print_report():
    #print report
    for key in res:
        print(f"Current Coffee Machine {key}: {res[key]}")

def transaction(coffee_name, coffee_cost):
    print(f"Great Choice! The {coffee_name} is: ${coffee_cost}")
    print("-"*110)

    payment = []
    print("Please input payment in the amounts of, [1] Penny ($0.01) [2] Nickel($0.05) [3] Dimes ($ 0.10) [4] Quarters ($0.25): ")
    transc = {"penny":0.01,
                "nickel":0.05,
                "dime":0.10,
                "quarter":0.25}

    for key in transc:
        try:
            paid_coins = int(input(f"{key.capitalize()}(Number of {key.capitalize()}/s): "))
        except ValueError:
            print("An error during transaction occured, Refunding & closing transaction ... ")
            print(f"Total coins refunded: {sum(payment)}")
            return False

        payment.append(transc[key] * paid_coins)
    print("="*110)
    print("Processing Transaction...")
    

    change = sum(payment) - coffee_cost

    if change < 0:
        print("="*110)
        print("Transaction Failed...")
        print("-"*110)
        print("Sorry that's not enough money. Money refunded.")
        print(f"Total coins refunded: {sum(payment)}")
        print("="*110)
        return False

    else: 
        print("="*110)
        print("Transaction successful ...")
        print("-"*110)
        print(f"Total coins recieved: ${sum(payment)}")
        print(f"- {coffee_name}({coffee_cost})\nChange: {change}")
        return True
    
print(logo)
while power:
    
    #initialize blank resource dictionary
    res_cache = {}

    print("="*110)
    print("Note: type 'report' to generate report of the current coffee machine resources, 'off' to turn off the program")
    print("-"*110)


    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off": 
        power = False
        print(thanks)
    elif user_input == "report":
        print_report()
        power = True
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        
        #selected menu values 
        u_water = menu[user_input]["ingredients"]["water"]
        u_milk = menu[user_input]["ingredients"]["milk"]
        u_coffee = menu[user_input]["ingredients"]["coffee"]
        u_cost = menu[user_input]["cost"]

        coffee_lease = transaction(user_input.capitalize(), u_cost )

        
        if coffee_lease == True:
        #res_k == Coffee Machine resources
            res_w= res["water"]
            res_m= res["milk"]
            res_c= res["coffee"]

            res_cache["water"] = res_w - u_water
            res_cache["milk"] = res_m - u_milk
            res_cache["coffee"] = res_c - u_coffee
        
            #the cache's value is now the res value
            res = res_cache

            print("Thank you! Enjoy your coffee & have a nice day!")
            
    else:
        print("\n"*20, logo)
        print("Invalid choice ... Restarting transaction")


             


