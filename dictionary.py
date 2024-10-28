# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 2

Created on Mon Aug 19 17:26:05 2024

@author: Bailey Byl 20135558
"""


# Returns a dictionary with 12 actors and their birth date
def create_dictionary_actors():
    actor_dictionary = {'Dwayne Johnson':'22-5-1972',
                  'Tom Cruise':'13-09-1978',
                  'Johnny Deep':'01-03-1969',
                  'Robert Downey Jr':'26-03-1987',
                  'Leonardo Dicaprio':'16-12-1983',
                  'Henry Cavil':'12-05-1975',
                  'Chris Hemsworth':'22-04-1984',
                  'Chris Evans':'26-08-1986',
                  'Hugh Jackman':'03-05-1972',
                  'Morgan Freeman':'06-07-1991',
                  'Keanu Reeves':'12-10-1987',
                  'Tom Hanks':'22-02-1981'}
    return actor_dictionary
    
# Returns a dictionary with 12 movies and their release year
def create_dictionary_movies():
    movie_dictionary = {'Alien: Romulus':2021,
                  'Deadpool & Wolverine':2022,
                  'Twisters':2023,
                  'Sonic the Hedgehog 3':2020,
                  'Inside Out 2':2019,
                  'Borderlands':2021,
                  'Alien':1999,
                  'A Quiet Place: Day One':2013,
                  'The Fall Guy':2024,
                  'Hit Man':2015,
                  'Despicable Me 4':2023,
                  'Gladiator II':2018}
    return movie_dictionary

# Returns a dictionary with 12 games and their release year
def create_dictionary_games():
    game_dictionary = {'Counter-Strike 2':2023,
                 'Dota 2':2017,
                 'Apex Legends':2019,
                 'Grand Theft Auto V':2013,
                 'Rust':2016,
                 'Team Fortress 2':2013,
                 'Minecraft':2011,
                 'Elden Ring':2020,
                 'Rainbow Six Siege':2019,
                 'Dead by Daylight':2021,
                 'Overwatch 2':2023,
                 'Red Dead Redemption 2':2020}
    return game_dictionary

# Appends a value to a dictionary
def add_value_to_dictionary(key, value, dictionary):
    dictionary[key] = value
    
# Removes a value from a dictionary
def delete_value_from_dictionary(key, dictionary):
    try:
        dictionary.pop(key)
        return True
    except:
        return False
    
# Sorts a dictionary in ascending order
def sort_dictionary_ascending(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items()))
    return sorted_dictionary

# Sorts a dictionary in descending order
def sort_dictionary_descending(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items(), reverse=True))
    return sorted_dictionary
    
# Searches a dictionary for a value and returns its location, or -1 if it cannot find it
def search_dictionary(key, dictionary):
    if key in dictionary:
        return list(dictionary).index(key)
    else:
        return False


def main():
    print('Dictionary Manipulation Program by Bailey Byl 20135558')
    option = None
    # Main user dictionary variable that gets manipulated
    user_dictionary = None
    while True:
        print('''Options:
              C - Create/Change/Reset dictionary
              A - Append value to the dictionary
              D - Delete a value from the dictionary
              S - Sort the dictionary
              F - Find a value in the dictionary
              P - Print the dictionary
              ENTER to exit
              ''')
        option = str(input("Option: "))
        
        # Allows the user to create a dictionary from 3 presets - actors, movies or games
        if option == 'C' or option == 'c':
            while True:
                print('''Dictionary types:
                      A - Actor dictionary
                      M - Movie dictionary
                      G - Game dictionary
                      ENTER to go back''')
                option_dictionary = str(input("Option: "))
                if option_dictionary == 'A' or option_dictionary == 'a':
                    user_dictionary = create_dictionary_actors()
                    print('Actor dictionary created!')
                    break
                elif option_dictionary == 'M' or option_dictionary == 'm':
                    user_dictionary = create_dictionary_movies()
                    print('Movie dictionary created!')
                    break
                elif option_dictionary == 'G' or option_dictionary == 'g':
                    user_dictionary = create_dictionary_games()
                    print('Game dictionary created!')
                    break
                elif option_dictionary == '':
                    break
                else:
                    print('Invalid option')
        
        # Allows the user to add a value to the dictionary they have created
        elif option == 'A' or option == 'a':
            if user_dictionary == None:
                print('No dictionary has been created, create one first')
            else:
                key = str(input("Enter the key to add: "))
                value = str(input("Enter the value to add: "))
                if value == '' or key == '':
                    print('Nothing has been added to the dictionary')
                else: 
                    add_value_to_dictionary(key, value, user_dictionary)
                    print(key, ':', value, 'has been added to the dictionary')
        
        # Allows the user to remove a value from the dictionary they have created
        elif option == 'D' or option == 'd':
            if user_dictionary == None:
                print('No dictionary has been created, create one first')
            else:
                key = str(input("Enter the key to remove: "))
                if key == '':
                    print('Nothing has been removed the dictionary')
                else: 
                    if delete_value_from_dictionary(key, user_dictionary):
                        print(key, 'has been removed from the dictionary')
                    else:
                        print(key, 'is not in the dictionary')
        
        # Allows the user to sort the dictionary, either in ascending or descending order
        elif option == 'S' or option == 's':
            if user_dictionary == None:
                print('No dictionary has been created, create one first')
            while True:
                print('''Options:
                      A - Ascending order
                      D - Decending order
                      ENTER to go back''')
                option_sort = str(input('Option: '))
                if option_sort == 'A' or option_sort == 'a':
                    user_dictionary = sort_dictionary_ascending(user_dictionary)
                    print('dictionary has been sorted in ascending order')
                    break
                elif option_sort == 'D' or option_sort == 'd':
                    user_dictionary = sort_dictionary_descending(user_dictionary)
                    print('dictionary has been sorted in descending order')
                    break
                elif option_sort == '':
                    break
                else:
                    print('Invalid option')
            
        # Allows the user to search for the value in the dictionary and returns the location, or tells the user it isn't in the dictionary if it cannot be found    
        elif option == 'F' or option == 'f':
            if user_dictionary == None:
                print('No dictionary has been created, create one first')
            while True:
                search_key = input('Enter key to search for: ')
                result = search_dictionary(search_key, user_dictionary)
                if result == False:
                    print('Item not in the dictionary')
                    break
                else:
                    print('Item in the dictionary at position', result)
                    break
        
        # Prints out the full dictionary
        elif option == 'P' or option == 'p':
            print(user_dictionary)
            
        elif option == '':
            break
        
        else:
            print('Invalid option')
        
    print('Exiting the program...')

if __name__ == "__main__":
    main()
    