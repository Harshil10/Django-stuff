import sys, os

'''
@author = Harshil Modi
'''

'''
Decorator function to take inputs from User
'''
def decorate_input(func):
    arr = []
    def inner():
        elem_count = raw_input('Enter Number of elements to Sort: ')
        for i in xrange(0, int(elem_count)):
            elem = raw_input()
            arr.append(int(elem))
        func(arr)
    return inner
