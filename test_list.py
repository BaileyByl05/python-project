# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 2

Created on Mon Aug 19 17:25:59 2024

@author: Bailey Byl 20135558
"""

import unittest

from list import create_list_actors, create_list_games,create_list_movies,add_value_to_list,delete_value_from_list,sort_list_ascending,sort_list_descending,search_list

class TestListFunctions(unittest.TestCase):
    
    def test_create_list_games(self):
        test_list = create_list_games()
        self.assertEqual(test_list, ['Counter-Strike 2','Dota 2','Apex Legends','Grand Theft Auto V','Rust','Team Fortress 2','Minecraft','Elden Ring','Rainbow Six Siege','Dead by Daylight','Overwatch 2','Red Dead Redemption 2'])
    
    def test_create_list_movies(self):
        test_list = create_list_movies()
        self.assertEqual(test_list, ['Alien: Romulus','Deadpool & Wolverine','Twisters','Sonic the Hedgehog 3','Inside Out 2','Borderlands','Alien','A Quiet Place: Day One','The Fall Guy','Hit Man','Despicable Me 4','Gladiator II'])
        
    def test_create_list_actors(self):
        test_list = create_list_actors()
        self.assertEqual(test_list, ['Dwayne Johnson','Tom Cruise','Johnny Deep','Robert Downey Jr','Leonardo Dicaprio','Henry Cavil','Chris Hemsworth','Chris Evans','Hugh Jackman','Morgan Freeman','Keanu Reeves','Tom Hanks'])
        
    def test_add_value(self):
        test_list = []
        add_value_to_list('test', test_list)
        self.assertEqual(test_list, ['test'])
        
    def test_delete_value_true(self):
        test_list = ['test1','test2']
        delete_value_from_list('test2', test_list)
        self.assertEqual(test_list, ['test1'])
        
    def test_delete_value_false(self):
        test_list = ['test1','test2']
        delete_value_from_list('test3', test_list)
        self.assertEqual(test_list, ['test1','test2'])
        
    def test_sort_ascending_letters(self):
        test_list = ['a','d','c','z']
        sort_list_ascending(test_list)
        self.assertEqual(test_list, ['a','c','d','z'])
        
    def test_sort_descending_letters(self):
        test_list = ['a','d','c','z']
        sort_list_descending(test_list)
        self.assertEqual(test_list, ['z','d','c','a'])
        
    def test_sort_ascending_numbers(self):
        test_list = [1,5,3,7]
        sort_list_ascending(test_list)
        self.assertEqual(test_list, [1,3,5,7])
        
    def test_sort_descending_numbers(self):
        test_list = [1,5,3,7]
        sort_list_descending(test_list)
        self.assertEqual(test_list, [7,5,3,1])
        
    def test_search_list_true(self):
        test_list = ['a','b','c']
        self.assertEqual(search_list('b', test_list), 1)
        
    def test_search_list_false(self):
        test_list = ['a','b','c']
        self.assertEqual(search_list('d', test_list), -1)
        

if __name__ == '__main__':
    unittest.main()