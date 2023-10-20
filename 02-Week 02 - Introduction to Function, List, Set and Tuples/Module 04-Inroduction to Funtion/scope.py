balance = 500

def total_cost(price,quantity):
    global balance
    cost = price*quantity
    remaining = balance-cost
    balance = cost
    print(remaining)
    return cost

print(f'Balance : outsite : {balance}')
pay=total_cost(10,3)
print(f'Please pay : {pay}')