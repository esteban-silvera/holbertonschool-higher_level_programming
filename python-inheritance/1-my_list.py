#!/usr/bin/python3
"""una lista que hereda una lista"""
class MyList(list):
    """una lista my rey"""

    def print_sorted(self):
        print(sorted(self))
