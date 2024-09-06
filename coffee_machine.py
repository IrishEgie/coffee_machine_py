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


print(logo)
while power:
    #initialize blank resource dictionary
    res_cache = {}


    print("Note: type 'report' to generate report of the current coffee machine resources, 'off' to turn off the program")
    print("="*110)


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
        print(f"This is the selected menu's cost is: ${u_cost}")
        print("-"*110)
        payment = int(input("Please input payment [1] Penny ($0.01) [2] Nickel($0.05) [3] Dimes ($ 0.10) [4] Quarters ($0.25): "))

    
        #res_k == Coffee Machine resources
        res_w= res["water"]
        res_m= res["milk"]
        res_c= res["coffee"]

        res_cache["water"] = res_w - u_water
        res_cache["milk"] = res_m - u_milk
        res_cache["coffee"] = res_c - u_coffee
        
        #the cache's value is now the res value
        res = res_cache
            
    else:
        break

print("\n"*20, logo)
print("Invalid choice ... Restarting transaction")
             


