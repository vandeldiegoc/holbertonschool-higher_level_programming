#!/usr/bin/python3
"""rectangle"""
from models.base import Base

class Rectangle(Base):
    """class inherits"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width of the value> must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height  must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y of the value> must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """return area"""
        return (self.__width * self.__height)
    


    def display(self):
        """print display"""
        for y in range(self.__height):
            for x in range(self.__width):
                print ('#', end="")
            print()

    def __str__(self):
        '''print str'''
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
        self.id, self.__x, self.__y,self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''update value'''
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """rectangle dicionary"""
        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y
        return dictionary

