actual_cost = [22000]             #actual cost
sale_amount = [21550]              #sale amount
product_sale = zip(actual_cost, sale_amount)
for actual_cost, sale_amount in product_sale:   #the product is for sale
    if actual_cost < sale_amount:
        print("profit:", actual_cost-sale_amount)
    elif actual_cost > sale_amount:
        print("loss:", sale_amount-actual_cost)
        

