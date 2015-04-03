import sys, os
from functools import wraps

'''
@author = Harshil Modi
'''

'''
Decorator function to take inputs from User
'''
def list_input():
    arr = []
    elem_count = raw_input('Enter Number of elements to Sort: ')
    for i in xrange(0, int(elem_count)):
        elem = raw_input()
        arr.append(int(elem))
    return arr

def decorate_input(argument):
    def inner(func):
        @wraps(func)
        def inner_most():
            if argument == 'list':
                array = list_input()
                func(array)
        return inner_most
    return inner
