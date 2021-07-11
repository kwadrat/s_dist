#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
Template file for testing functions and classes
./dist.py test; red_green_bar.py $? $COLUMNS
'''

import sys
import unittest


def thresh(value):
    return (6 * (value + 100) / 50)


class Box:
    def __init__(self):
        '''
        Box:
        '''
        self.ls = []

    def add(self, value, tm=None):
        '''
        Box:
        Dodaj kolejną wartość do listy
        '''
        if tm is not None and tm > thresh(value):
            self.ls = [value]
        else:
            if value not in self.ls:
                self.ls.append(value)
                if len(self.ls) > 2:
                    if (
                            abs(self.ls[2] - self.ls[0])
                            > abs(self.ls[2] - self.ls[1])):
                        del self.ls[0]
                    else:
                        del self.ls[1]

    def get(self):
        '''
        Box:
        Wyznacz średnią wartość listy
        '''
        if self.ls:
            return sum(self.ls) / (len(self.ls))
        else:
            return None


class TestDist(unittest.TestCase):
    def test_something(self):
        '''
        TestDist:
        '''
        obk = Box()
        obk.add(10, 0)
        self.assertEqual(obk.get(), 10)
        obk.add(12)
        self.assertEqual(obk.get(), 11)

    def test_second(self):
        '''
        TestDist:
        '''
        obk = Box()
        obk.add(20)
        obk.add(30)
        self.assertEqual(obk.get(), 25)
        obk.add(40)
        self.assertEqual(obk.get(), 35)

    def test_third(self):
        '''
        TestDist:
        Pomiń element bardziej odległy (czyli drugi)
        '''
        obk = Box()
        obk.add(2)
        obk.add(10)
        obk.add(0)
        self.assertEqual(obk.get(), 1)

    def test_four(self):
        '''
        TestDist:
        Jeśli element jest już na liście jako
        pierwszy, to zignoruj ten nowy element.
        '''
        obk = Box()
        obk.add(2)
        obk.add(10)
        obk.add(2)
        self.assertEqual(obk.get(), 6)

    def test_fifth(self):
        '''
        TestDist:
        Jeśli element jest już na liście w dowolnym
        miejsciu, to zignoruj ten nowy element.
        '''
        obk = Box()
        obk.add(2)
        obk.add(10)
        obk.add(10)
        self.assertEqual(obk.get(), 6)

    def test_sixth(self):
        '''
        TestDist:
        Wyrzuć wszystkie elementy jeśli czas jest
        większy niż 10 sekund
        '''
        obk = Box()
        obk.add(2)
        obk.add(10)
        obk.add(30, 12)
        self.assertEqual(obk.get(), 20)

    def test_seventh(self):
        '''
        TestDist:
        Obsługa pustej listy
        '''
        obk = Box()
        self.assertEqual(obk.get(), None)

    def test_ninth(self):
        '''
        TestDist:
        '''
        self.assertEqual(thresh(15), 13.8)
        self.assertEqual(thresh(16), 13.92)


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        unittest.main(argv=sys.argv[:1])
