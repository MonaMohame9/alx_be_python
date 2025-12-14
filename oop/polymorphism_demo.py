# polymorphism_demo.py
# Demonstration of polymorphism with Shape, Rectangle, and Circle classes

import math

class Shape:
    """Base class for all shapes"""
    def area(self):
        """Method to compute area. Must be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle shape class"""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle"""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class"""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * (self.radius ** 2)
