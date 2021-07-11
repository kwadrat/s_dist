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
        Dodaj kolejną wartość do listy
        '''
        self.ls.append(value)
        if len(self.ls) > 2:
            del self.ls[0]

    def get(self):
        '''
        Skrzynka:
        Wyznacz średnią wartość listy
        '''
        return sum(self.ls) / (len(self.ls))


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

    def test_second(self):
        '''
        TestDist:
        '''
        obk = Skrzynka()
        obk.add(20)
        obk.add(30)
        self.assertEqual(obk.get(), 25)
        obk.add(40)
        self.assertEqual(obk.get(), 35)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
