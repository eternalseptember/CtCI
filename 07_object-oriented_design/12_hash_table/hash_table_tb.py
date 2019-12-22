from hash_table import *

# The first name is key, and the value is the last name.
test_set_1 = [
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

test_set_2 = [
    ('Mia', 'Mann'),
    ('Tim', 'King'),
    ('Bea', 'Stone'),
    ('Zoe', 'Rice'),
    ('Sue', 'Steele'),  # conflicts with Mia
    ('Len', 'Bell')  # conflicts with Tim
    ]

test_hash = Hash_Table(11)

for item in test_set_1:
    key, value = (item)
    test_hash.insert(key, value)


print(test_hash)

