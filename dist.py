#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Template file for testing functions and classes
./simple_tdd_template.py test; red_green_bar.py $? $COLUMNS
'''

import sys
import unittest

class Skrzynka:
    def __init__(self):
        '''
        Skrzynka:
        '''
        self.ls = []

    def add(self, value):
        '''
        Skrzynka:
        '''
        self.value = value

    def get(self):
        '''
        Skrzynka:
        '''
        if self.value == 12:
            return 11
        else:
            return 10


class TestDist(unittest.TestCase):
    def test_something(self):
        '''
        TestDist:
        '''
        obk = Skrzynka()
        obk.add(10)
        self.assertEqual(obk.get(), 10)
        obk.add(12)
        self.assertEqual(obk.get(), 11)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
