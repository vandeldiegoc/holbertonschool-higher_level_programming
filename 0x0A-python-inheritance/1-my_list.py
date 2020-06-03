#!/usr/bin/python3
"""that is a module that has a class"""

class MyList(list):
    """new class"""
    
    def print_sorted(self):
        """print list sorted"""
        print(sorted(self))
