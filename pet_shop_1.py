item_arr = {
    "collar" : {
        "id" : 1, 
        "name" : "Dog collar",
        "price": 15
    },
    "dog_bed" : {
        "id" : 2, 
        "name" : "Dog bed",
        "price" : 50
    },
    "dog_food" : {
        "id" : 3, 
        "name" : "Doggy food",
        "price" : 7
    },
    "cat_bed" : {
        "id" : 4, 
        "name" : "Cat bed",
        "price" : 45
    },
    "cat_food" : {
        "id" : 5, 
        "name" :"Katty food",
        "price" : 7
    },
    "shampoo" : {
        "id" : 6, 
        "name" : "Pet shampoo",
        "price" : 15
    },
    "brushes" : {
        "id" : 7,
        "name" : "Pet brushes",
        "price" : 12
    }
}
user_action_sele = ''
user_cart = []
user_cart_unit = {}
cart_item_id = 0
list_item_id = []
total = 0
print("-" * 50)
print("Welcome to Paws n Cart")
print("-" * 50)

flag = False

while flag == False:
    print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
    user_action_sele = input("Enter number of the option you want to select: ")
    if user_action_sele.isnumeric():
        user_action_sele = int(user_action_sele)
        if user_action_sele == 1:
            inner_flag = False
            while inner_flag is False:
                print("-" * 50)
                print("Select from our products:")
                for c1 in item_arr:
                    print(f"Item: {item_arr[c1]['id']}\t {item_arr[c1]['name'].ljust(15)}: £ {item_arr[c1]['price']}")
                user_item_sele = input("Select number of desired item: ")
                print("-" * 50)
                if user_item_sele.isnumeric():
                    user_item_sele = int(user_item_sele)
                    for ele in item_arr:
                        if item_arr[ele]["id"] == user_item_sele:
                            total += item_arr[ele]["price"]
                            cart_item_id += 1
                            list_item_id.append(cart_item_id)
                            user_cart_unit = dict(item_arr[ele]) 
                            user_cart.append(user_cart_unit)
                            inner_flag = True
                        if user_item_sele > len(item_arr) or user_item_sele < 1:
                            print("No entry can be higher than the last id item or lower than 1.")
                            break
                else:
                    print("-" * 50)
                    print("Please, enter valid item number!")
                    print("-" * 50)
           
        elif user_action_sele == 2:
            remove_flag = False
            while remove_flag is False:
                print("-" * 50)
                print("Remove item:")
                for c2 in user_cart:
                    print(f"id: {c2['id']}\t {c2['name']}" .ljust(27)+" : £ ",c2['price']) 
                
                user_remove = input("Enter the id number of the item you want to remove or 'q' to quit: ")
                print("-" * 50)
                if user_remove.isnumeric(): 
                    user_remove = int(user_remove)
                    c = 1
                    for i in user_cart:
                        
                        if user_remove == i["id"]:
                            total -= i["price"]
                            user_cart.remove(i)
                            print(f"You have removed item: {i['name']} : £ {i['price']}")
                            print("-" * 50)
                            remove_flag = True
                 
                        if user_remove != i['id'] and c == len(user_cart):
                            print("Please, enter a valid digit!")
                        c += 1
                else:
                    if user_remove.lower() == 'q':
                        remove_flag = True
                    else:
                        print("-" * 50)
                        print("Enter a valid id number!")
                        print("-" * 50)
                
        elif user_action_sele == 3:
            
            print("-" * 50)
            print("Shop list:\n")
            for c3 in user_cart:
                
                print(f"id: {c3['id']}\t {c3['name']}" .ljust(27)+" : £",c3['price'])
                
            print("-" * 50)
            print("Total".ljust(30)+": £", total) 
            print("=" * 50)   
            
        elif user_action_sele == 4:
            print("-" * 50)
            print("Checkout:")
            for c4 in user_cart:
                print(f"id: {c4['id']}\t {c4['name']}" .ljust(27)+" : £",c4['price'])
                
            print("-" * 50)
            print("Total".ljust(30)+": £", total) 
            print("-" * 50)
            flag = True
            print("=" * 50)  
            
        if user_action_sele < 0 or user_action_sele > 4:
            print("-" * 50)
            print('Please, insert correct digit!')
            print("-" * 50)
               
    else:
        print('-'* 50)
        print("Wrong entry! Enter a valid input!")
        print('-'* 50)