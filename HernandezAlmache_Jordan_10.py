
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 10


'''
(1)Build 2 new methods into the shopping cart class,
    -write_reciept_to_file()
     create the file obj. in the name of the customer asnd write the cart info into a xt file stored on the system.
     i. First and final line of the file should say "---RECIEPT---"
     ii.Customer name and date
     iii.Number of items
     iv.Print item cost
     v.Print item description
     vi.Print total price

    -view_reciept_file()
     a. Read the contents of the txt file stored in the previous step and print
     b.if the file is not found on the system, output a msg by using try and except: File not found.

(2)Implement two new options in the print_menu() functions. So, your new print_menu() funtion should print
f - Finalize order
v - View Receipt
'''
class ShoppingCart:
    count = 0

    def __init__(self,customer_name,current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        ShoppingCart.count += 1

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

    def print_descriptions(self):
        for list_a in self.cart_items:
            for items in list_a:
                for description in items:
                    print(description,': ',items[description][2])
        print('Number of Items:{}'.format(order.count))

    def remove_item(self, item_name):
        ###Removing item by key
        count_b = 0
        for list_a in self.cart_items:
            for items in list_a:
                if item_name in items:
                    count_b += 1
                    items.pop(item_name, 0)
                print(items)
        if count_b == 0:
            print('Item not found in the cart')

    def modify_item(self,ItemToPurchase):
        ###Dealing with input to find key
        for names in ItemToPurchase:
            for x in names:
                name = x
        ###Modifing dict with key and new_qty        
        count_c = 0
        for list_a in self.cart_items:
            for items in list_a:
                for names in items:
                    if names == name:
                        print(names)
                        count_c += 1
                        print(self.cart_items[0][0][name][0]) 
                        new_qty = ItemToPurchase[0][item][0]
                        self.cart_items[0][0][name][0] = new_qty
                        print(self.cart_items) 
                   
        if count_c == 0:
            print('Item not found in the cart')

    def write_reciept_to_file(self):
        #create a reciept file
        file_name = self.customer_name + '.txt'
        file_name = file_name.replace(" ","")
        customer_order = open(file_name, 'w')
        customer_order.write("---RECIEPT---\n\n")
        customer_order.write(self.customer_name + ', ' + self.current_date + '\n\n')

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
                    customer_order.write('{}, {} @ ${:.2f} = ${:.2f}\n'.format(qty,quantity,price,amount))
                    customer_order.write('- Item Description: '+ items[qty][2] + '\n')
                    
        customer_order.write('\nQuantity of Items: {}\n'.format(item_count))            
        customer_order.write('Total: ${:.2f}\n\n'.format(amount_count))
        customer_order.write("---RECIEPT---")
        customer_order.close()
        
    def view_reciept_to_file(self):
     #a. Read the contents of the txt file stored in the previous step and print
     #b.if the file is not found on the system, output a msg by using try and except: File not found.

        file_name = self.customer_name + '.txt'
        file_name = file_name.replace(" ","")
        try:
            customer_order = open(file_name, 'r')
            lines = customer_order.readlines()
            customer_order.close()
          
            for w in lines:
                print(w)
        except:
            print('File not Found.') 

class LessThanZerroError(Exception):
    def __init__(self, value):
        self.value = value

#menu    
def print_menu():
    print('\nMENU\n\
    a - Add item to cart\n\
    r - Remove item from the cart\n\
    c - Change item quantity\n\
    i - output item\'s description\n\
    o - output shopping cart\n\
    f - Finalize order\n\
    v - View Receipt\n\
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

        if command == 'a':
            
            try:
                print('ADD ITEM TO CART')
                item = str(input('Enter the item name:'))
                description = str(input('Enter the item description:'))
              
                try:
                    price = float(input('Enter the item price:'))
                    quantity = int(input('Enter the item quantity:'))
                    print(price)
                    print(quantity)
                    if quantity <= 0:
                        raise LessThanZerroError('Invalid: entry less than 0.')
                    elif price <= 0:
                        raise LessThanZerroError('Invalid: entry less than 0.')
                    elif price == chr:
                        raise TypeError('Invalid: character instead of integer/float.')
                    elif quantity == chr:
                        raise TypeError('Invalid: character instead of integer/float.')
                    elif quantity == float:
                        raise TypeError('Invalid amount: float instead of integer.')
                
                except ValueError as excpt:
                    print(excpt)
                    print('Invalid Entry')
                except TypeError as excpt:
                    print(excpt)
                    print('Invalid Entry')
                ItemToPurchase = [{item:[quantity,price,description]}]
                order.add_item(ItemToPurchase)
            
            #except LessThanZerroError as excpt:
            #    print(excpt)
            #    print('Invalid Entry')
            #except ValueError as excpt:
            #    print(excpt)
            #    print('Invalid Entry')
            #except TypeError as excpt:
            #    print(excpt)
            #    print('Invalid Entry')
            except Exception as e:
                print(e)
           # except TypeError:
               # print('Invalid: character instead of integer/float.'')
        elif command == 'r':
            item_name = str(input('Enter the name of the item to remove:'))
            order.remove_item(item_name)

        elif command == 'c':
            item = str(input('Enter the name of the item to be changed:'))
            print('MODIFY ITEM TO CART')
            description = '0'
            price = 0.00
            quantity = int(input('Enter the item quantity:'))

            ItemToPurchase = [{item:[quantity,price,description]}]

            order.modify_item(ItemToPurchase)

        elif command == 'i':
            print('OUTPUT ITMES\' DESCRIPTIONS')
            print('{}\'s Shopping Cart - {}'.format(customer_name,current_date))
            print('Items Descriptions')
            order.print_descriptions()

        elif command == 'f':
            order.write_reciept_to_file()
            print('RECEIPT SUCCESSFULLY WRITTEN TO FILE\n')
            sub_command = input('Are you sure you are done shopping(y/n)?')
            if sub_command != 'n':
                break

        elif command == 'v':
            print('VIEW RECEIPT')
            order.view_reciept_to_file()

        elif command == 'o':
            print('OUTPUT SHOPPING CART')
            print('{}\'s Shopping Cart - {}'.format(customer_name,current_date))
            order.get_cost_of_cart()

    except Exception as e:
        #print('Could not calculate info(a).\n')
        print(e)
    command = print_menu()








