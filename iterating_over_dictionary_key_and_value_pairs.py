__author__ = 'Taio'

# dict.iteritems
# Use dict.items in Python 3

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for k, v in m.iteritems():
    print '{}: {}'.format(k, v)