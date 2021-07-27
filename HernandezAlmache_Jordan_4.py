
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 4

#1 Prompt the user to enter a sentence. Store the txt as a str. After user input, the prog. should output #the entered str before printing options in (Part2).
#    Ex.Please enter a sentence:
#        ...
#        You entered:The most certain way to succeed is to always try one more time!

#2 Display a Menu, as shown in the example below. Each option is represenetd by a single char.
#    Ex. MENU
#        c - Number of non-whitespace characters.
#        w - Number of words.
#        r - Reverse the order of the words.
#        q - Quit.
#        Choose an option:
#if an invalid char is entered, continue to prompt for a valid choise. Continue to display menu options #until the user enters q to Quit.

#3 Implement a function to count and return the number of chars in the str, exclude all whitespace.
#    Ex. Number of non-shitespace characters:{}

#4 Implement a function to return the number of words in the str
#    Ex. Number of non-shitespace characters:{}

#5 Implement a function to reverse each word of the entered sentence to display the sentence in reverse. 
#    Ex. Output:time! more one try always to is succeed to way certain most The

def white_space(main_sentence):
    count = 0 
    for i in main_sentence:
        if(i.isalnum()):
            count += 1 
    return count

def num_words(main_sentence):
    words = len(main_sentence.split(' '))
    return words

def reverse_order(main_sentence):
    words = main_sentence.split(' ')
    rev_words = words[::-1]
    new_sentence = ' '.join(rev_words)
    print(new_sentence)
    return

    return new_sentence

main_sentence = input('Please enter a sentence:')
print('\nYou entered:', main_sentence)

option = 0
while option != 'q':
    print('\nMENU\n' 
        'c - Number of non-whitespace characters.\n'
        'w - Number of words.\n'
        'r - Reverse the order of the words.\n'
        'q - Quit.\n')
    option = input('\nChoose an option:')

    if option == 'c':
        count = white_space(main_sentence)
        print(count)
          
    elif option == 'w':
        words = num_words(main_sentence)
        print(words)
          
    elif option == 'r':
        reverse_order(main_sentence)

    elif option != 'q':
        print('Invalid character,try again.')
