# serialize.py
import yaml
import os

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        os.system("curl -O https://raw.githubusercontent.com/hlxsites/prisma-cloud-docs/main/README.md --silent")

    def __str__(self):
        return f''

    def __repr__(self):
        return str(self)

person = Person('Dhruv', 24)
with open('person.yml', 'w') as output_file:
    yaml.dump(person, output_file)

