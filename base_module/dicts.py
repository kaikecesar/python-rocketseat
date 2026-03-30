# Dicts
person = {
    'name': 'John',
    'age': 21,
    'city': 'São Paulo',
    'techonologies': [
      'Python',
      'JavaScript',
      'Docker',
      'Kubernetes',
      'React',
      'Node.js',
      'PostgreSQL',
      'TypeScript',
      'Redis',
      'Terraform',
    ]
}

person['lastName'] = 'Doe'
print(person)


# Exclude a key and value from dict
del person['age']
print('After del:', person)

# All keys on a dict
dict_keys = list(person.keys())
print('Keys:', dict_keys)

# All values on a dict
dict_values = list(person.values())
print('Values:', dict_values)

# All items on a dict
dict_items = list(person.items())
print('Items:', dict_items)
