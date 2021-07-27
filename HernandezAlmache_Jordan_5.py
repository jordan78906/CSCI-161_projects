
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 5

###1. Prompt the user to enter the title for the dataset table. Output the title.
###2. Prompt the user for the headers of two columns of a table. Output the column headers.
'''
3. Prompt the user for data. Data must be in this format: str, int. Store the information before the comma into a string variable and the information after the comma into an integer. The user will enter -1 when they have finished entering data. output the data. Store the str components of the data in a list of str. Store the integer components of the data in a list of integers
'''
'''
4. Perform error cheching for the data point entries. if any of the following errors occurs, output the appropropriate error message and prompt again for a valid data point.
-If entry has no comma                         Output: Error: No comma in string.
-If entry has more than one comma              Output: Error: Too many commas in input.
-If entry after the comma is not an integer    Output: Error: Comma not followed by an integer.

case 1

case 2

case 3

case 4
'''
'''
5. Output the information in a formatted table. The title is right justified with a minimum field. width value of 33. column 1 has a minimum field width value of 20. column 2 has a minimum field width calue of 23.(Hint: You can use this command to align the title, print('%33s'%Title))
'''
###1###
Title = input('Enter a title:')
print('You entered:',Title)
###2###
col1 = input('Enter the column 1 header:')
print('You entered:', col1) 
col2 = input('Enter the column 2 header:')
print('You entered:', col2)
###3###
main_list = []
Auther_Name = []
Num_of_Novels = []
new_entry = None
copy_main_list = []
copy_main_list2 = []

while new_entry != '-1':
    new_entry = input('Enter a data(-1 to stop input):')
    count = 0
    for x in new_entry:
        if x.isdigit():
            count += 1 
###4###
    if new_entry == '-1':
        continue

    elif ',' not in new_entry:
        print('Error: No comma in string.')
        print('Fix:', new_entry)   

    elif ',,' in new_entry:
        print('Error: Too many commas in input.')
        print('Fix:', new_entry)   

    elif count == 0:
        print('Error: Comma not followed by an integer.')
        print('Fix:', new_entry)

    else:
        copy_main_list = new_entry.split(',')
        print('Data String:' , copy_main_list[0])
        print('Data Integer:' , copy_main_list[1])
    
        Auther_Name.append(copy_main_list[0])
        Num_of_Novels.append(int(copy_main_list[1]))
###5###
print('%33s'%Title)
print('{col1:<20}|{col2:>23}'.format(col1=col1, col2=col2))
print('-' * 44)

final = zip(Auther_Name,Num_of_Novels)
for i,j in final:
    print('{col1:<20}|{col2:>23}'.format(col1 = i, col2 = j))


