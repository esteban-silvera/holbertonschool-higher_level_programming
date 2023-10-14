#!/usr/bin/python3
"""solo un rectangulo mi rey"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """solo un cuadrado mi rey"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(width, height, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
