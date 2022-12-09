#!/usr/bin/python3
"""Create fibonacci series upto n using lambda"""
fibonacci = lambda n: [0, 1] + [fibonacci(n-1)[i-1] + fibonacci(n-1)[i-2] for i in range(2, n)]

print(fibonacci(6))