import sys, os
from Decorators.input_user import decorate_input

'''
@author = Harshil Modi
'''

'''
Insertions Sort Algorithm Implementation
'''
#@decorate_input
#def anagram_problem():
    

@decorate_input('list')
def insertion_sort(ARR):
    for i in xrange(1, len(ARR)):
        #print ARR[i]
        for j in xrange(0, i):
            if ARR[i] == ARR[j]:
                continue
            elif ARR[i] < ARR[j]:
                ARR[i], ARR[j] = ARR[j], ARR[i]
        print ARR

insertion_sort()
