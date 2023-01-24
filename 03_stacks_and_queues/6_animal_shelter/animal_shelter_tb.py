# Test cases for the "animal shelter" problem.


from animal_shelter import *


# Setting up test case
shelter = AnimalShelter()
adoption_list = [
		 ('cat', 'cat_1'),
		 ('cat', 'cat_2'),
		 ('dog', 'dog_1'),
		 ('cat', 'cat_3'),
		 ('dog', 'dog_2'),
		 ('dog', 'dog_3'),
		 ('dog', 'dog_4'),
		 ('cat', 'cat_4'),
		 ('cat', 'cat_5'),
		 ('dog', 'dog_5'),
		 ('dog', 'dog_6'),
		 ]

for animal in adoption_list:
	shelter.enqueue(animal)

print('Animals in the shelter:')
print(shelter)
print()


# Dequeuing test
#requests = ['any', 'dog', 'cat', 'dog', 'dog', 'dog', 'cat', 'any']

# Dequeue all cats, dogs, any
#requests = ['cat', 'cat', 'cat', 'cat', 'cat', 'cat']
#requests = ['dog', 'dog', 'dog', 'dog', 'dog', 'dog', 'dog']
requests = ['any', 'any', 'any', 'any', 'any', 'any', 'any', 'any', 'any', 'any', 'any', 'any']


print('Adoption:')
for request in requests:
	if request == 'dog':
		item = shelter.dequeueDog()
		print('dequeue dog: {0}'.format(item))
	elif request == 'cat':
		item = shelter.dequeueCat()
		print('dequeue cat: {0}'.format(item))
	else:
		item = shelter.dequeueAny()
		print('dequeue any: {0}'.format(item))


# Results after dequeue requests
print('\nRemaining animals in the shelter:')
print(shelter)

