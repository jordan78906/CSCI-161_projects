
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 13
#Binary Search

#Linked lists and searching algorithms
'''
#Part 2: Searching Algorithm
#Linear Search or Binary Search
#Binary Search
1. Start with the middle element:
   a. if the target value is = to mid element of the array, then return the index of mid element
   b. if not, then compare the mid element with the target value,
      i.if the target value is > the num in the mid index, then pick the elements to the right
        of the mid index and start with step1
      ii.if the target value is < than the num in the mid index, then pick the elements to the 
        left of the mid index and start with Step 1
2. When a match is found, return the index of the element matched
3. If no match is found, then return -1

'''
def mergeSort(main_list):

    #1:Mid-Point - Slicing array in half
    #Left array from 0-mid    Right array from mid-end
    L_list = main_list[:len(main_list)//2]
    R_list = main_list[len(main_list)//2:]

    #4: Base Case - Already sorted, since its a single element.
    if len(main_list) <= 1:
        return main_list

    #2&3: Recursion - slices left & right arrays to the smaller arrays, length of 1 element  
    mergeSort(L_list)
    mergeSort(R_list)
    
    
    #5: Merge - Merge divided arrays sorted 
    merge_sorted_arrays(L_list,R_list,main_list)
    

def merge_sorted_arrays(L_list,R_list,main_list):
    #Merge
 
    #keeping track of index positions
    #i = left index, j = right index, k = merged index
    i = j = k = 0

    #Rebuilding main array with multiple smaller arrays of 1 element length
    #going through index positions in both L AND R array
    while i < len(L_list) and j < len(R_list):
        #comparison
        if L_list[i] <= R_list[j]:
            main_list[k] = L_list[i]
            #adding to main array and moving pointer on L_List array over 1
            i += 1
        else:
            main_list[k] = R_list[j]
            #adding to main array and moving pointer on R_List array over 1
            j += 1
        #Moving down the index of merged array, to keep adding elements
        k += 1

    #continues reading off L_list if R_list finishes first
    while i < len(L_list):
        main_list[k] = L_list[i]
        i += 1
        k += 1

    #continues reading off R_list if L_list finishes first
    while j < len(R_list):
        main_list[k] = R_list[j]
        j += 1
        k += 1



#requires an ordered list before searching through
def BinarySearch(num_list,key,low,high,indent):
   #print(indent,'BinarySearch()',low,high)
   range_size = (high-low) +1
   mid = (high+low)//2
   if key == num_list[mid]:
      #print(indent, 'Found Integer')
      pos = mid
   elif range_size == 1:
      #print(indent, 'Integer Not Found')
      pos = -1
   else:
      if key < num_list[mid]:
         #print(indent, 'Searching low half')
         pos = BinarySearch(num_list,key,low,mid,indent+'   ')
      else:
         #print(indent, 'Searching high half')
         pos = BinarySearch(num_list,key,mid+1,high,indent+'   ')

   
   #print(indent,'Returning pos = {}'.format(pos))
   #print(num_list[pos])
   return pos

num_list = [5,45,1,7,99,3]
indent = ''
command = 'y'
while command == 'y':
   i = int(input('Enter an integer value for your list:'))
   num_list.append(i)
   command = input('Would you like to add more values?(y or n)')
print (num_list)


mergeSort(num_list)
#print('\nSorted Array:')
#print(num_list)

command = 'y'
while command == 'y':
   j = int(input('\nPlease enter an integer value to search in the list:'))
   pos = BinarySearch(num_list,j,0,len(num_list),indent)
   if pos >= 0:
      print('Your value {}, was found in the list:-D'.format(j))
   else:
      print('Sorry, your value {}, was not found :-('.format(j))

   command = input('Would you like to search for another value?(y or n)')





