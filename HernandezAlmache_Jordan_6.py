
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 6

#1) This program will store and edit the roster and rating info for a soccer team. Similar to how coaches rate players during tryuots to ensure a balanced team. Prompt user for jersey num(0-99) and rating (1-9) for 5 players. Store the entries in the form of dict. print the dict. elements with the jersey num in ascending order(i.e. print the roster from smallest to largest num)HINT dict keys can be stored in a sorted list.
#2 Implement a menu of options for a user to mod the roster. Each option is represented by a single char. The program initially prints the menu and the program only ends when the user chooses the option to quit.

#4 For'Remove player' menu option, prompt the user for Jersey num. remove that player(jersey & rating)
#5 For 'Update a player rating' opt., prompt the user for a players jersey num. Prompt again for a new rating for the player, and then change the players rating.

#6 For 'List players above a certain rating' opt., prompt the user for a rating. Print the jersey num rating of all the players above the specific rating. Include the entry as well


#7 For 'Print roster' opt., print the updated roster.

#FIXME
#need to come back and re-write code to make it work!!!!!!!!!



def menu():
    print('MENU')
    print('a - Add a player.')
    print('d - Remove a player.')
    print('u - Update a player rating.')
    print('r - List players above a certain rating.')
    print('o - Print roster.')
    print('q - Quit.')

def roster():
    for player in players:
    
        jersey = players[player]['jersey']
        rating = players[player]['rating']
        #FIXME
        #for shirt in sorted(players[player]['jersey']):

        print('Jersey:{x:<10}Rating:{y:<1}'.format(x=jersey,y=rating))

players = {
    'player1' : {'jersey': 5, 'rating' : 0},
    'player2' : {'jersey': 4, 'rating' : 0},
    'player3' : {'jersey': 3, 'rating' : 0},
    'player4' : {'jersey': 2, 'rating' : 0},
    'player5' : {'jersey': 1, 'rating' : 0},
    }

count = 0
for player in players:
    count += 1
    new_jersey = input('Enter player {}\'s jersey number(0-99):'.format(count))
    new_ranting = input('Enter player {}\'s rating(1-9):'.format(count))
    players.update({player : {'jersey': new_jersey, 'rating' : new_ranting}})



roster()


print(list(players.values()))
player_values_list = list(players.values())
print(list(player_values_list.items()))

user_input = None

while user_input != 'q':
    menu()
    user_input = input('Choose an option: ')
    if user_input == 'a':
        print('Add new players stats.')
        count += 1
        new_player = 'player{}'.format(count)
        new_jersey = input('Enter player {}\'s jersey number:'.format(count))
        new_rating = input('Enter player {}\'s rating:'.format(count))
        players.update({new_player : {'jersey': new_jersey, 'rating' : new_ranting}})

    elif user_input == 'd':
        print('Remove a player & stats.')
        remove_player = input(int('Enter a Jersey Number:'))
        #FIXME
        for player, stats in players.items():
        players.update({player: {'jersey': new_jersey, 'rating' : new_ranting}})

    elif user_input == 'u':
        #FIXME
        print('Update a player's rating.')
        edit_player = input(int('Enter the Jersey Number for the player you want to update:'))

        new_rating = input(int('Enter the players new rating:'))
        players[player]['rating'].update(new_ranting)

    elif user_input == 'r':
        #FIXME
        players_above_rating = int('Enter a rating:')
        print('Players with rating above {}'.format(players_above_rating)


    elif user_input == 'o':
        roster()


