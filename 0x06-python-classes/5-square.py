#!/usr/bin/python3
'''class Square'''


class Square:
    """define class Square"""

    def __init__(self, size=0):
        """__Init__ data with error handling"""
        self.size = size

    def area(self):
        """Returns the square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns size of Square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size attribute"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Print stdout the square with #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
