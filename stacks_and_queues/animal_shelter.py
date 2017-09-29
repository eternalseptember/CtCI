"""
An animal shelter, which holds only dogs and cats, operates on a
strictly "first in, first out" basis. People must adopt either the
"oldest" (based on arrival time) of all animals at the shelter, or
they can select whether they would prefer a dog or a cat (and will
receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue,
dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
LinkedList data structure.
"""


class AnimalShelter:
    def __init__(self):
        self.master_queue = []
        self.cats_queue = []
        self.dogs_queue = []


    def enqueue(self, animal_type, animal):
        if animal_type == "cat":
            self.master_queue.append('cat')
            self.cats_queue.append(animal)
        else:
            self.master_queue.append('dog')
            self.dogs_queue.append(animal)


    def dequeueAny(self):
        oldest = self.master_queue.pop(0)
        if oldest == "cat":
            return self.cats_queue.pop(0)
        else:
            return self.dogs_queue.pop(0)


    def dequeueDog(self):
        print('\tdequeue dog', end=' ')
        print(self.master_queue.pop(0))
        return self.dogs_queue.pop(0)


    def dequeueCat(self):
        print('\tdequeue cat', end=' ')
        print(self.master_queue.pop(0))
        return self.cats_queue.pop(0)


    def __str__(self):
        return '{0}\n{1}\n{2}'.format(self.master_queue, self.cats_queue, self.dogs_queue)


# Setting up test case
shelter = AnimalShelter()
values = [
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
requests = ['any', 'dog', 'cat', 'dog', 'dog', 'dog', 'cat', 'any']

for value in values:
    animal, name = (value)
    shelter.enqueue(animal, name)

print('Animals in the shelter:')
print(shelter)
print()

# Dequeuing test
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

print('\nRemaining animals in the shelter:')
print(shelter)
