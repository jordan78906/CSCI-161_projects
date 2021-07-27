
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 7

#1 Online shopping cart. build a ItemToPurchase class with the following specs:
class ItemToPurchase:
    def __init__(self):
        self.items_name = 'none'
        self.items_description = 'none'
        self.items_price = 0
        self.items_quantity = 0

    def item_name(self):
        return(str(self.items_name))
    def item_description(self):
        return(str(self.items_description))
    def item_price(self):
        return(float(self.items_price))
    def item_quantity(self):
        return(int(self.items_quantity))

#2 implement the following methods for the ItemToPurchase class
    def print_item_cost(self): 
        print('{}, {} @ ${:.2f}'.format(self.item_name(),self.item_quantity(),self.item_price(),),end = '')
    def print_item_description(self):
        print('{}:\n    {}'.format(self.items_name,self.items_description))

#3 in the main section of your code, prompt the user to enter two items and create a two objects of the ItemToPurchase class.

item_1 = ItemToPurchase()
print('Enter data for Item 1:')
item_1.items_name = input('Please enter the item name for item:')
item_1.items_description = input('Please enter the item description:')
item_1.items_price = input('Please enter the item price:')
item_1.items_quantity = input('Please enter the item quantity:')

item_2 = ItemToPurchase()
print('Enter data for Item 2:')
item_2.items_name = input('Please enter the item name for item:')
item_2.items_description = input('Please enter the item description:')
item_2.items_price = input('Please enter the item price:')
item_2.items_quantity = input('Please enter the item quantity:')

#4 Add the costs of the two items together and output the total cost.
val1 = item_1.item_price() * item_1.item_quantity()
val2 = item_2.item_price() * item_2.item_quantity()
total = val1 + val2


print('\nTOTAL COST')
item_1.print_item_cost()
print(' = ${:.2f}'.format(val1))
item_2.print_item_cost()
print(' = ${:.2f}'.format(val2))
print('Total: ${:.2f}'.format(total))

#5 Print out the items along with their descriptions.

print('\nItem Descriptions:')
item_1.print_item_description()
item_2.print_item_description()

