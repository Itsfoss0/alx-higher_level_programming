#!/usr/bin/python3
def print_square(size):
    """ Function to print squares of '#'
    Args:
        size(int/float) -> number of "#"'s to print
                        -> Must be an int or a float >= 0
    Returns nothing except if an exception occured,
    in which case the exception raised is returned
    """
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(size, float) and size < 0:
            raise ValueError("size must be an integer")
        else:
            for row in range(size):
                for column in range(size):
                    print("#", end="")
                print()
    except Exception as e:
        return (e)
