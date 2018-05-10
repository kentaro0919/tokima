#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A Utility for python code I use many times.
"""
import datetime
import calendar


def flatten(nested_list):
    """This function receive a nested list and return a single list"""
    return [e for inner_list in nested_list for e in inner_list]


class TokimaDate(object):
    
    def __init__(self, year=None, month=None):
        self.year = int(year)
        self.month = int(month)
        self.year_month = "{}-{:0>2}".format(self.year, self.month)
        self.day_numbers = calendar.monthrange(self.year, self.month)[1]
    
    def first_day(self):
        return datetime.date(self.year, self.month, 1).strftime('%Y-%m-%d')
    
    def last_day(self):
        return datetime.date(self.year, self.month, self.day_numbers).strftime('%Y-%m-%d')

