print("hello")

"""
>>> my_summer(5,3)
120
"""
def my_summer( x ,y):
    """
    >>> [my_summer(n , n * n) for n in range(6)]
    [0, 2, 6, 12, 20, 30]

    >>> my_summer(1,0)
    1


    >>> my_summer(1,1)
    1

    >>> my_summer(1,2)
    3
    """

    
    
    return x + y



import doctest
if __name__ == "__main__":
    doctest.testmod()