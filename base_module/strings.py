# String format
fullname = input('Type your full name: ')
print('Welcome', fullname)
print('Welcome ' + fullname)
print('Welcome %s' % fullname)
print(f'Welcome {fullname}')
print('Welcome {}'.format(fullname))

print('To Upper', fullname.upper())
print('To Lower', fullname.lower())

print('First Character', fullname[0])
print('Last Character', fullname[-1])

print('Count character repeating...', fullname.count('a'))

print('Show position of a character', fullname.find('e')) # Always the first returned

print('Replace strings', fullname.replace('a', 'o'))
