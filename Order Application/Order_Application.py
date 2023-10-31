menu=['Pizza £7.30', 'Pie £3.45', 'Burger £4,50', 'Chips £2.00', 'Onion Rings:£2.30', 'Drink £1.50'] # i created the menu and added the prices and items in the list 

for menus in menu: # this will loop will print the list so the user knows the prices and the items avabile
    print(menus)



total_cost=0.0 # this code is a variable for the total cost and its price
order_items=[] #here is where  the items that the user will chose will be added
ordering=True #here i created the oredring variable ,this line will make the loop from below work because i set the value True 

while ordering: 
    user_order=input('What would you like to order?(after you finish you order just type Finish):  ').lower()#this will ask the user to input his order lower means that whateever he wrotes will be converted in lowercase and if  he types finish the code will break
    if user_order=='finish':
        break
    elif user_order=='pizza':
        total_cost+=7.30
        order_items.append(menu[0])
        print('Pizza has been added to your order') #the rest of the code will check whatever the user typed in will add it to the order items list and will add the price to the total cost also will show what items has been added
    elif user_order=='pie':
        total_cost+=3.45
        order_items.append(menu[1])
        print('A pie  has been added to your order')
    elif user_order=='burger':
        total_cost+=4.50
        order_items.append(menu[2])
        print('A Burger has been added to your order')
    elif user_order=='chips':
        total_cost+=2.00
        order_items.append(menu[3])
        print('Chips have been added to your order')
    elif user_order=='onion rings':
        total_cost+=2.30
        order_items.append(menu[4])
        print('Onion rings  have been added to your order')
    elif user_order=='drink':
        total_cost+=1.50
        order_items.append(menu[5])
        print('A drink has been added to your order')

print('Your order is ') # this will print what the order items are 
for orders in order_items:
    print(orders)

print(f'Your total is £{total_cost}') #this will print the total cost 
print('Thank You For Ordering From Us!')#this is the ending text 
    
