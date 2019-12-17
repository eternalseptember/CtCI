from hash_table import *

# The first name is key, and the value is the last name.
test_set = [
    ('Jan', 'Graves'),
    ('Tim', 'King'),
    ('Mia', 'Mann'),
    ('Sam', 'French'),
    ('Leo', 'Moody'),
    ('Ted', 'Wise'),
    ('Bea', 'Stone'),
    ('Lou', 'Ward'),
    ('Ada', 'Cross'),
    ('Max', 'Grant'),
    ('Zoe', 'Rice')
    ]

test_hash = Hash_Table(11)

for item in test_set:
    key, value = (item)
    test_hash.insert(key, value)


print(test_hash)

