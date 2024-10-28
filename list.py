# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 2

Created on Mon Aug 19 17:26:05 2024

@author: Bailey Byl 20135558
"""

# Returns a list with 12 actors
def create_list_actors():
    actor_list = ['Dwayne Johnson',
                  'Tom Cruise',
                  'Johnny Deep',
                  'Robert Downey Jr',
                  'Leonardo Dicaprio',
                  'Henry Cavil',
                  'Chris Hemsworth',
                  'Chris Evans',
                  'Hugh Jackman',
                  'Morgan Freeman',
                  'Keanu Reeves',
                  'Tom Hanks']
    return actor_list
    
# Returns a list with 12 movies
def create_list_movies():
    movie_list = ['Alien: Romulus',
                  'Deadpool & Wolverine',
                  'Twisters',
                  'Sonic the Hedgehog 3',
                  'Inside Out 2',
                  'Borderlands',
                  'Alien',
                  'A Quiet Place: Day One',
                  'The Fall Guy',
                  'Hit Man',
                  'Despicable Me 4',
                  'Gladiator II']
    return movie_list

# Returns a list with 12 games
def create_list_games():
    game_list = ['Counter-Strike 2',
                 'Dota 2',
                 'Apex Legends',
                 'Grand Theft Auto V',
                 'Rust',
                 'Team Fortress 2',
                 'Minecraft',
                 'Elden Ring',
                 'Rainbow Six Siege',
                 'Dead by Daylight',
                 'Overwatch 2',
                 'Red Dead Redemption 2']
    return game_list

# Appends a value to a list
def add_value_to_list(value, list):
    list.append(value)
    
# Removes a value from a list
def delete_value_from_list(value, list):
    try:
        list.remove(value)
        return True
    except:
        return False
    
# Sorts a list in ascending order
def sort_list_ascending(list):
    list.sort()

# Sorts a list in descending order
def sort_list_descending(list):
    list.sort(reverse=True)
    
# Searches a list for a value and returns its location, or -1 if it cannot find it
def search_list(value, list):
    if value in list:
        return list.index(value)
    else:
        return -1

def main():
    print('List Manipulation Program by Bailey Byl 20135558')
    option = None
    # Main user list variable that gets manipulated
    user_list = None
    while True:
        print('''Options:
              C - Create/Change/Reset List
              A - Append value to the list
              D - Delete a value from the list
              S - Sort the list
              F - Find a value in the list
              P - Print the list
              ENTER to exit
              ''')
        option = str(input("Option: "))
        
        # Allows the user to create a list from 3 presets - actors, movies or games
        if option == 'C' or option == 'c':
            while True:
                print('''List types:
                      A - Actor list
                      M - Movie list
                      G - Game list
                      ENTER to go back''')
                option_list = str(input("Option: "))
                if option_list == 'A' or option_list == 'a':
                    user_list = create_list_actors()
                    print('Actor list created!')
                    break
                elif option_list == 'M' or option_list == 'm':
                    user_list = create_list_movies()
                    print('Movie list created!')
                    break
                elif option_list == 'G' or option_list == 'g':
                    user_list = create_list_games()
                    print('Game list created!')
                    break
                elif option_list == '':
                    break
                else:
                    print('Invalid option')
        
        # Allows the user to add a value to the list they have created
        elif option == 'A' or option == 'a':
            if user_list == None:
                print('No list has been created, create one first')
            else:
                value = str(input("Enter the value to add: "))
                if value == '':
                    print('Nothing has been added to the list')
                else: 
                    add_value_to_list(value, user_list)
                    print(value, 'has been added to the list')
        
        # Allows the user to remove a value from the list they have created
        elif option == 'D' or option == 'd':
            if user_list == None:
                print('No list has been created, create one first')
            else:
                value = str(input("Enter the value to remove: "))
                if value == '':
                    print('Nothing has been removed the list')
                else: 
                    if delete_value_from_list(value, user_list):
                        print(value, 'has been removed from the list')
                    else:
                        print(value, 'is not in the list')
        
        # Allows the user to sort the list, either in ascending or descending order
        elif option == 'S' or option == 's':
            if user_list == None:
                print('No list has been created, create one first')
            while True:
                print('''Options:
                      A - Ascending order
                      D - Decending order
                      ENTER to go back''')
                option_sort = str(input('Option: '))
                if option_sort == 'A' or option_sort == 'a':
                    sort_list_ascending(user_list)
                    print('List has been sorted in ascending order')
                    break
                elif option_sort == 'D' or option_sort == 'd':
                    sort_list_descending(user_list)
                    print('List has been sorted in descending order')
                    break
                elif option_list == '':
                    break
                else:
                    print('Invalid option')
            
        # Allows the user to search for the value in the list and returns the location, or tells the user it isn't in the list if it cannot be found    
        elif option == 'F' or option == 'f':
            if user_list == None:
                print('No list has been created, create one first')
            while True:
                search_value = input('Enter value to search for: ')
                result = search_list(search_value, user_list)
                if result == -1:
                    print('Item not in the list')
                    break
                else:
                    print('Item in the list at position',result)
                    break
        
        # Prints out the full list
        elif option == 'P' or option == 'p':
            print(user_list)
            
        elif option == '':
            break
        
        else:
            print('Invalid option')
        
    print('Exiting the program...')
    
if __name__ == "__main__":
    main()


