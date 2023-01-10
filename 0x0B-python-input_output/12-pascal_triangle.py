#!/usr/bin/python3

"""Function to print pascal's triangle upto level <n>"""


def pascal_triangle(n):
    """Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
