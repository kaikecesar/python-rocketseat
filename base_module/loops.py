# Loop for
for i in range(10):
    print(i)

# Loop while
i = 0
while i < 10:
    print(i)
    i += 1

# Loop in a dict
person = {
    'name': 'John',
    'age': 21,
    'city': 'São Paulo',
}
for key, value in person.items():
    print(f'{key}: {value}')
