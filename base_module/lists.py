# Lists
technologies = [
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

# Add a item on list
technologies.append('React Native')
print(technologies)

# Show the index of an element
print(technologies.index('Node.js'))

# Insert an element on a specific index
technologies.insert(1, 'GoLang')
print('After insert:', technologies)

# Remove and return an item of a specific index
removed_by_pop = technologies.pop(1)  # Removes de previews item
print('Removed by pop:', removed_by_pop)

# Remove the first element with the provided value
technologies.remove('React')
print('After remove:', technologies)

# Sort a list
technologies.sort()
print('After sort:', technologies)

# Reverse a list
technologies.reverse()
print('After reverse:', technologies)

# Clear a list
technologies.clear()
print('After clear:', technologies)
