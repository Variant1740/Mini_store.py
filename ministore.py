#mini store management system
import time
store={
    'Ps5': 350,
    'Ps4': 250,     #price in dollars
    'Ps Controllers': 50,
    'Airpods': 75,
}

cart={}

print('''
      WELCOME TO MINIMART-GAMING ONLINE STORES Inc.
      PROCEED TO REGISTER:
      ''')

name=input('NAME: ').upper()
print('Loading...')
for x in range(0, 3):
    time.sleep(1)

print(f'Welcome {name}')
password=input('Create a password: ')
print('Loading...')
for x in range(0, 3):
    time.sleep(1)

prompt=input('Do you want to save your password?(YES OR NO): ').upper()
if prompt=="YES":
    print('''
        Password Saved.
        You would not need to enter your password on your next log-in.
          ''')
else:
    pass
print(f'Welcome {name}')
print('Please Wait, the menu display would pop up shortly...')
for x in range(0, 7):
    time.sleep(1)


while True:
    print('''
             STORE ITEMS:
          1. View Items
          2. Add item to Cart
          3. Purchase Items
          4. Remove Items from Cart
          5. Display Cart
          6. Display Receipt
          7. Exit
          ''')
    
    choice=input('Select an action: ')

    if choice=='1':
        print('Available items:')
        for item, price in store.items():
            print(f'- {item} : ${price:,}')
        #for key, value in store.items():
            #print(key,':' ,'$',value)

    elif choice=='2':       
        print('Available items:')
        for item, price in store.items():
        #for item, price in store.items():
            print(f'- {item}')
        while True:
            choice2=input('What Item do you want to add?(Q to quit): ').title()
            if choice2=='Q':
                break
            if choice2 in store:  
                cart[choice2]= 1
                print(f"{choice2} has been added to your cart at ${store[choice2]}")
                
            else:
                print('Only Items in store can be added to cart')
            
        

    elif choice=='3':
        print('\nAvailable items:')
        for item, price, in cart.items():
            print(f'{item} ')
        while True:
            choice3=input('Which item do you want to buy?(Q to quit): ').title()
            if choice3=='Q':
                break
            if choice3 in store:
                quantity= int(input(f"How many {choice3} do you want to purchase?: "))
                if choice3 in cart:
                    cart[choice3]+=quantity
            #print(store.get(choice2))
                    print(f" {quantity} {choice3} has been purchased\n COST:${(store.get(choice3))*quantity}")
                else:
                    cart[choice3]=quantity
                    print(f" {quantity} {choice3} has been purchased\n COST:${(store.get(choice3))*quantity}")
            else:
                print('Sorry, that item is not in the store')

    elif choice=='4':
        choice4=input('Which item do you want to remove?: ').title()
        if choice4 in cart:
            del cart[choice4]
            print(f"{choice4} has been removed from your Cart")
        else:
            print('item is not in your cart')
    
    elif choice=='5':
        print('Your Cart: ')
        for key, value in cart.items():
            print(key, '-', "quantity=", value)
    
    elif choice=='6':
        if not cart:
            print('Your cart is empty. NO receipt to display')
        else:
            print("===== RECEIPT =====")
            total_amount=0
            for item, quantity in cart.items():
                #price=store[item]
                price=store[item]
                cost=price*quantity
                total_amount+=cost
                print(f'{item} x{quantity} = ${cost:,}')

            print('--------------')
            print(f'TOTAL = ${total_amount:,}')
            print('============')
    
        
    elif choice=='7':
        print('Thamk you for purchasing from us')
        break
    