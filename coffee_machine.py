import menu as m
import art
import transaction as tr
#initialize global variables here
menu = m.menu #is dictionary
res = m.resources  #is dictionary
logo = art.logo #is multiline string
thanks = art.fin
power = True #is bool

#res_k == Coffee Machine resources
res_water= res["water"]
res_milk= res["milk"]
res_coffee= res["coffee"]
res_money= res["money"]

print(logo)
while power:
    
    #initialize blank resource dictionary
    res_cache = {}

    print("="*110)
    print("Note: type 'report' to generate report of the current coffee machine resources, 'off' to turn off the program")
    print("-"*110)


    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off": 
        tr.print_report(res)
        power = False
        print(thanks)
    elif user_input == "report":
        tr.print_report(res)
        power = True
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        coffee = menu[user_input]
        #selected menu values 
        u_water = coffee["ingredients"]["water"]
        u_milk = coffee["ingredients"]["milk"]
        u_coffee = coffee["ingredients"]["coffee"]
        u_cost =coffee["cost"]
        
        res_check = tr.check_resources(res, coffee)

        if res_check == True:
        #wrap this inside an if statement if the coffe machine still has enough resources for a another batch of coffee
            coffee_lease = tr.transaction(user_input.capitalize(), u_cost)
            
            # print(coffee_lease)
            if coffee_lease:
                res_money += u_cost
                res_cache["water"] = res_water - u_water
                res_cache["milk"] = res_milk - u_milk
                res_cache["coffee"] = res_coffee - u_coffee
                res_cache["money"] = res_money - coffee_lease

                #the cache's value is now the res value
                res = res_cache

                print("Thank you! Enjoy your coffee & have a nice day!")
        else:
            print("Sorry! This coffee machine does not have enough resources to complete you order. Closing transaction ... ")
            power = False
            print(thanks)
    else:
        print("\n"*20, logo)
        print("Invalid choice ... Restarting transaction")


             


