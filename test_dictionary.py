# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 2

Created on Mon Aug 19 17:26:20 2024

@author: Bailey Byl 20135558
"""

import unittest

from dictionary import create_dictionary_actors, create_dictionary_games, create_dictionary_movies, add_value_to_dictionary, delete_value_from_dictionary, sort_dictionary_ascending, sort_dictionary_descending, search_dictionary

class TestDictionaryFunctions(unittest.TestCase):
    
    def test_create_dictionary_games(self):
        test_dictionary = create_dictionary_games()
        self.assertEqual(test_dictionary, {'Counter-Strike 2':2023,
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
                     'Red Dead Redemption 2':2020})
    
    def test_create_dictionary_movies(self):
        test_dictionary = create_dictionary_movies()
        self.assertEqual(test_dictionary, {'Alien: Romulus':2021,
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
                      'Gladiator II':2018})
        
    def test_create_dictionary_actors(self):
        test_dictionary = create_dictionary_actors()
        self.assertEqual(test_dictionary, {'Dwayne Johnson':'22-5-1972',
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
                      'Tom Hanks':'22-02-1981'})
        
    def test_add_value(self):
        test_dictionary = {'test1':'value1'}
        add_value_to_dictionary('test2', 'value2', test_dictionary)
        self.assertEqual(test_dictionary, {'test1':'value1','test2':'value2'})
        
    def test_delete_value_true(self):
        test_dictionary = {'test1':'value1','test2':'value2'}
        delete_value_from_dictionary('test2', test_dictionary)
        self.assertEqual(test_dictionary, {'test1':'value1'})
        
    def test_delete_value_false(self):
        test_dictionary = {'test1':'value1'}
        result = delete_value_from_dictionary('test2', test_dictionary)
        self.assertEqual(test_dictionary, {'test1':'value1'})
        self.assertEqual(result, False)
        
    def test_sort_ascending_letters(self):
        test_dictionary = {'a':0,'d':2,'c':1,'z':3}
        sort_dictionary_ascending(test_dictionary)
        self.assertEqual(test_dictionary,{'a':0,'c':1,'d':2,'z':3})
        
    def test_sort_descending_letters(self):
        test_dictionary = {'a':3,'d':1,'c':2,'z':0}
        sort_dictionary_descending(test_dictionary)
        self.assertEqual(test_dictionary, {'z':0,'d':1,'c':2,'a':3})
        
    def test_search_dictionary_true(self):
        test_dictionary = {'a':1,'b':2,'c':3}
        self.assertEqual(search_dictionary('b', test_dictionary), 1)
        
    def test_search_dictionary_false(self):
        test_dictionary = {'a':1,'b':2,'c':3}
        self.assertEqual(search_dictionary('d', test_dictionary), False)
        

if __name__ == '__main__':
    unittest.main()
