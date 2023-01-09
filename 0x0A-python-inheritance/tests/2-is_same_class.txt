=======================
How to Use 2-is_same_class.py
=======================

This module defines a function ```is_same_class``` that asserts if a object is an instance of the class

==========
Test
===========

>>> is_same_class = __import__('2-is_same_class').is_same_class

>>> is_same_class()
Traceback (most recent call last):
...
TypeError: is_same_class() missing 2 required positional arguments: 'obj' and 'a_class'

>>> is_same_class("John", str)
True

>>> is_same_class(1, int)
True

>>> is_same_class(1, float)
False
