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
	('Len', 'Bell'),  # conflicts with Tim
	('Mit', 'Watt'),  # conflicts with Tim
	('Nel', 'Ice'),  # conflicts with Tim
	('Jan', 'Graves'),
	('Liz', 'Barnes'),  # conflicts with Jan
	('Rex', 'Boon')  # conflicts with Jan
	]

test_hash = Hash_Table(11)

# for item in test_set_1:
for item in test_set_2:
	key, value = (item)
	test_hash.insert(key, value)

print('\t\tOriginal test hash')
print(test_hash)
print()

# =============================================================================

test_set_3 = [
	('Tim', 'Sand'),  # update Tim (head of the chain)
	('Bea', 'Snow'),  # update Bea (no chain)
	('Len', 'Fly'),  # update Len (within the chain)
	('Mit', 'Pym')  # update Mit (end of chain)
	]

for item in test_set_3:
	key, value = (item)
	test_hash.insert(key, value)

print('\t\tUpdating values')
print(test_hash)
print()

# =============================================================================

test_get = [
	'Ada',  # not found
	'Zoe',  # single node at the root
	'Mia',  # root node
	'Len',  # middle of the chain
	'Mit'  # end of the chain
	]

print('\t\tGetting values')
for item in test_get:
	value = test_hash.get(item)
	print(value)
print()

# =============================================================================

test_delete = [
	'Bea',  # only node
	'Mia',  # first node
	'Nel',  # last node
	'Len',  # middle node
	'Geo',  # no-entry
	'Rex',
	'Jan',
	'Liz'
]

print('\t\tDeleting keys')
for item in test_delete:
	deleted = test_hash.delete(item)
	print('Deleting {0}: {1} ...'.format(item, deleted))
	print('\tHash after delete')
	print(test_hash)
	print()



