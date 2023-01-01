===============================
4-print_square.py
==============================

Usage:
    The print_square function takes one argument
    a) size(int) -> The size of the square. 
                 -> Must be an int or a float >= 0 
    and prints the square to standard output
Tests:

    >>> print_square = __import__('4-print_square').print_square

    >>> print_square(3)
    ###
    ###
    ###
    
    >>> print_square(2.0)
    TypeError('size must be an integer')

    >>> print_square(name)
    Traceback (most recent call last):
    ...
    NameError: name 'name' is not defined

    >>> print_square()
    Traceback (most recent call last):
    ...
    TypeError: print_square() missing 1 required positional argument: 'size'

    >>> print_square(None)
    TypeError('size must be an integer')

    >>> print_square(0)
    

    >>> print_square(-1)
    ValueError('size must be >= 0')

    >>> print_square(3.1)
    TypeError('size must be an integer')
