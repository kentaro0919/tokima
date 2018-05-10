#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase
from tokima.tokima import flatten
from tokima.tokima import TokimaDate


class TestTokimaDate(TestCase):
    
    def test_TokimaDate_str(self):
        tokima = TokimaDate(year="2018", month="6")
        self.assertEqual(tokima.month, 6)
        self.assertEqual(tokima.year, 2018)
        self.assertEqual(tokima.year_month, "2018-06")
        self.assertEqual(tokima.first_day(), "2018-06-01")
        self.assertEqual(tokima.last_day(), "2018-06-30")
        self.assertEqual(tokima.day_numbers, 30)
        
    def test_TokimaDate_num(self):
        tokima = TokimaDate(year=2018, month=6)
        self.assertEqual(tokima.month, 6)
        self.assertEqual(tokima.year, 2018)
        self.assertEqual(tokima.year_month, "2018-06")
        self.assertEqual(tokima.first_day(), "2018-06-01")
        self.assertEqual(tokima.last_day(), "2018-06-30")
        self.assertEqual(tokima.day_numbers, 30)

  
class TestTokima(TestCase):

    def test_flatten(self):
        self.assertEqual( flatten([["a", "b"], ["c", "d"]]), ["a", "b", "c", "d"])
        self.assertNotEqual(flatten([["a", "b"], ["c", "d"]]), ["a", "b", "c"])