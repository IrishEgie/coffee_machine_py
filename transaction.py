def transaction(coffee_name, coffee_cost):
    print(f"Great Choice! The {coffee_name} is: ${coffee_cost}")
    print("-"*110)

    payment_temp = []
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
            print(f"Total coins refunded: {sum(payment_temp)}")
            return False

        payment_temp.append(transc[key] * paid_coins)
    print("="*110)
    print("Processing Transaction...")
    
    payment = sum(payment_temp)


    change = payment - coffee_cost

    if change < 0 or payment>4.0:
        print("="*110)
        print("Transaction Failed...")
        print("-"*110)
        print("Sorry not enough money for coffee or payment has exceeded the machine acceptance amount ($4). Money refunded.")
        print(f"Total coins refunded: ${format(payment,".2f")}")
        
        return False

    else: 
        print("="*110)
        print("Transaction successful ...")
        print("-"*110)
        print(f"Total coins recieved: ${payment}")
        print(f"Coffee: {coffee_name} (${coffee_cost})\nChange: {change}")
        return change
    

def print_report(res):
    #print report
    print("="*110)
    print("Current Coffee Machine Resources")
    print("-"*110)
    for key in res:
        print(f"{key}: {res[key]}")
    print("="*110)



def check_resources(res, coffee_res):
    
    keys = ["water", "milk","coffee"]
    print("Checking resources ...")
    for key in keys:
        res[key] - coffee_res["ingredients"][key]
        curr_res = res[key] - coffee_res["ingredients"][key]
        #print(f"{res[key] } - {coffee_res["ingredients"][key]}: {curr_res}") 
        if curr_res < 0: 
            return False
    return True