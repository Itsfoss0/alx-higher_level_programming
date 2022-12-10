#!/usr/bin/python3
"""create a list that's consisted of lengths of each element in the first list"""
backend = ["Django", "Node", "Spring", "FastAPI", "Rails"]
backend_len = list(map(len, backend))
print(backend_len)