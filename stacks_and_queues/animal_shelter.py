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
        self.queue_num = 0
        self.cats_queue = []
        self.dogs_queue = []


    def enqueue(self, animal):
        animal_type, name = (animal)
        adoption_entry = (self.queue_num, name)

        if animal_type == "cat":
            self.cats_queue.append(adoption_entry)
        else:
            self.dogs_queue.append(adoption_entry)
        self.queue_num += 1


    def dequeueAny(self):
        num_of_cats = len(self.cats_queue)
        num_of_dogs = len(self.dogs_queue)

        if (num_of_cats == 0) and (num_of_dogs != 0):
            # if there are no cats
            return self.dequeueDog()
        elif (num_of_cats != 0) and (num_of_dogs == 0):
            # if there are no dogs
            return self.dequeueCat()
        else:
            first_dog = self.dogs_queue[0]
            dog_id, dog_name = (first_dog)
            first_cat = self.cats_queue[0]
            cat_id, cat_name = (first_cat)

            if cat_id < dog_id:
                return self.dequeueCat()
            else:
                return self.dequeueDog()


    def dequeueDog(self):
        try:
            adoptee = self.dogs_queue.pop(0)
            id_num, name = (adoptee)
            return name
        except IndexError:
            return None


    def dequeueCat(self):
        try:
            adoptee = self.cats_queue.pop(0)
            id_num, name = (adoptee)
            return name
        except IndexError:
            return None


    def __str__(self):
        return '{0}\n{1}'.format(self.cats_queue, self.dogs_queue)


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
requests = ['any', 'dog', 'cat', 'dog', 'dog', 'dog', 'cat', 'any']

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
