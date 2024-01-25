import yaml

# class Person needs to be present in the scope
with open('person.yml', 'r') as input_file:
    person = yaml.load(input_file, Loader = yaml.SafeLoader)

print(person)
