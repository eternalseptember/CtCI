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


for item in test_set:
    key, value = (item)
    hash_table.insert(key, value)

