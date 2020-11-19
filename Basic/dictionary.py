d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])

print('cat' in d)

d['fish'] = 'wet'
print(d['fish'])
del d['fish']

for key, value in d.items():
    print('A %s has %s' % (key, value))
