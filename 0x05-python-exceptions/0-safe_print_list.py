#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0 
    try:
        for i in range(x+1):
            print(my_list[i], end="")
            count += 1
            
    except IndexError:
        print("Index is out of range")
    finally:
        return (count)
