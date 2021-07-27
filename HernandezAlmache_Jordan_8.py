
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 8

'''
1. Build the ShoppingCart class with the following data attributes and related methods.
Note: Some methods can be empty stubs(empty methods) initially, which can be completed in the later steps. Also, a parameterized
constructor will take the customer's name and date as parameters.
2. in the main section of your code, prompt the user for a customer's name and todays date. print the name and date.
 create an object of type ShoppingCart
3. implement the print_menu() function. print_menu() has a ShoppingCart parameter and prints a menu of options to 
manipulate the shopping cart. each option is represented by a single character. build and print the menu within the
 function. if an invalid char is entered, continue to promt for a valid choice. 
Hint: implement quit before implementing other options. call print_menu() in the main() function. continue to execute
 the menu until the user enters q to quit.
'''
class ShoppingCart:
    count = 0
#attribute:
    def __init__(self,customer_name,current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    #methods
    #adds an item to the cart_items list. has parameter ItemToPurchase. Does not return anything
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        ShoppingCart.count += 1

    #calculates and returns the total cost of items in the cart. has no parameters
    def get_cost_of_cart(self):
        amount_count = 0
        item_count = 0
        for list_a in self.cart_items:
            for items in list_a:
                for qty in items:
                    amount = float(items[qty][0] * items[qty][1])
                    quantity = int(items[qty][0])
                    price = float(items[qty][1])
                    amount_count += amount
                    item_count += quantity
                    print('{}, {} @ ${:.2f} = ${:.2f}'.format(qty,quantity,price,amount))

        print('\nQuantity of Items: {}'.format(item_count))            
        print('Total: ${:.2f}'.format(amount_count))
        if amount_count == 0:
            print('Shopping Cart is Empty')

    #Prints each item's description
    def print_descriptions(self):
        for list_a in self.cart_items:
            for items in list_a:
                for description in items:
                    print(description,': ',items[description][2])
        print('Number of Items:{}'.format(order.count))

#menu    
def print_menu():
    print('\nMENU\n\
    a - Add item to cart\n\
    i - output item\'s description\n\
    o - output shopping cart\n\
    q - quit\n')
    commands = str(input('Enter a menu option: '))
    commands = commands.lower()
    return commands



####main####

customer_name = str(input('Enter the customer\'s name: '))
current_date = str(input('Enter today\'s date(MMM DD, YYYY):'))
print('\nCustomer name: {}'.format(customer_name))
print('Today\'s date: {}'.format(current_date))

order = ShoppingCart(customer_name,current_date)
command = print_menu()


while command != 'q':
    try:

        #6 Implement add item to cart menu option
        if command == 'a':
            print('ADD ITEM TO CART')
            item = str(input('Enter the item name:'))
            description = str(input('Enter the item description:'))
            price = float(input('Enter the item price:'))
            quantity = int(input('Enter the item quantity:'))         
            ItemToPurchase = [{item:[quantity,price,description]}]
            order.add_item(ItemToPurchase)

        #5 implement Output items description menu option
        elif command == 'i':
            print('OUTPUT ITMES\' DESCRIPTIONS')
            print('{}\'s Shopping Cart - {}'.format(customer_name,current_date))
            print('Items Descriptions')
            order.print_descriptions()

        #4 implement output shopping cart menu option.
        elif command == 'o':
            print('OUTPUT SHOPPING CART')
            print('{}\'s Shopping Cart - {}'.format(customer_name,current_date))
            order.get_cost_of_cart()

    except:
        print('Could not calculate info.\n')
        
    command = print_menu()








