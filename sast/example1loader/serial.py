# serialize.py
import yaml
import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'

    def __repr__(self):
        return str(self)
