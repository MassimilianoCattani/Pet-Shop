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
user_cart =[]
user_cart_names = []
user_cart_prices = []
cart_item_id = 0
list_item_id = []
# num_id_item = 0 There is no need to declare this var here.
total = 0

print("-" * 50)
print("Welcome to Paws n Cart")
print("-" * 50)

flag = False
print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
user_action_sele = int(input("---> Enter number of the option you want to select: "))

while flag == False:

    if user_action_sele == 1:
        
        print("Select from our products:")
        
        for i in item_arr:
            print(f"Item: {item_arr[i]['id']}\t {item_arr[i]['name'].ljust(15)}: £ {item_arr[i]['price']}")

        user_item_sele = int(input("---> Select number of desired item: "))
        
        for ele in item_arr:
            if item_arr[ele]["id"] == user_item_sele:
                cart_item_id += 1
                user_item = f". {item_arr[ele]['name'].ljust(20)}: £ {item_arr[ele]['price']}"
                list_item_id.append(cart_item_id - 1)
                user_cart.append(user_item)
                user_cart_names.append(item_arr[ele]["name"])     
                user_cart_prices.append(item_arr[ele]["price"]) 
                total += item_arr[ele]["price"]
        
        print("-" * 50)
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: "))  
        print("=========================================================================================") 
            
    elif user_action_sele == 2:

        num_id_item = 0
        arr_ids = []

        for k in user_cart:
            num_id_item += 1
            arr_ids.append(num_id_item)
            print(f"{num_id_item} {k}") 
            
        user_remove = int(input("---> Enter the number of the item you want to remove: "))
       
        for checker in range(len(arr_ids)):
            if user_remove == arr_ids[checker]:
                user_cart.remove(user_cart[user_remove - 1])
                total = total - user_cart_prices[user_remove - 1]
                user_cart_prices.remove(user_cart_prices[user_remove - 1])
    
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: "))   
        print("=========================================================================================")  
            
    elif user_action_sele == 3:
        
        print("Cart list:")

        for counter in user_cart:
            print(counter)
            
        print("-" * 50)
        print("Total".ljust(22)+": £", total) 
        print("-" * 50)
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: ")) 
        print("=========================================================================================")  
           
    elif user_action_sele == 4:
        
        print("Checkout:")

        for j in user_cart:
            print(j)
        
        flag = True
        print("-" * 50)
        print("Total".ljust(22)+": £", total) 
        print("-" * 50)
        print("=========================================================================================")  
        
    else:
        print('Please, insert correct digit')
        print("Would you like to: \n1. Add an item to your cart.\n2. Remove an item from your cart.\n3. View total cost of your cart.\n4. Checkout.")
        user_action_sele = int(input("---> Enter number of the option you want to select: ")) 
        print("=========================================================================================") 