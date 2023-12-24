# Sets in Python.
# We can say they work like tuples, but they are not ordered but they dont have duplicates.
# T hey are mutable. 
# Or we can say they work like dictionaries, but they don't have keys.
# They also have an immutable version, called frozenset .
# Creating a set using {}.
diamonds_card = {1,3,4,5,5}
# Set does not allow duplicates.
print(diamonds_card)
print(type(diamonds_card))
# Since it is not ordered we can access it through index.
# print(diamonds_card[0]) # TypeError: 'set' object is not subscriptable
# It can be accessed randomly in a loop.
for x in diamonds_card:
    print(x)

# Sets work well when you think about them as mathematical sets.

whole_set = {1,2,3,4,5,6}
odd_set = {1,3,5}
even_set = {2,4,6}

# Intersection
print('Intersection')
print(odd_set & whole_set) #{1.3,5}
print(even_set & whole_set) #{2,4,6}
print(odd_set & even_set) #{} or set()  ------> empty set
print(odd_set & even_set & whole_set) # set()

# You can create a union of two sets.
students = {'Leo','Tina','Mai','Mia','Soon'}
physics_students = {'Tina','Mai'}
chemistry_students = {'Tina','Leo','Soon'}
mathematics_students = {'Leo','Tina','Mai','Mia','Soon'}

# Some certificate physics or mathematics.
print(physics_students | mathematics_students) # {'Leo','Tina','Mai','Mia','Soon'}

# Bie certificate the student should be bothh in physics and mathematics.
# Qualified students
print('qualified students - common among the sets - intersection')
print(physics_students & mathematics_students) # {'Tina','Mai'}
print('dis qualified students - difference among the sets - difference')
print(mathematics_students - physics_students) # {'Leo', 'Soon', 'Mia'}

# Superset
print(mathematics_students > physics_students) # True
print('physics students is a subset of students.')
print(students > physics_students) # True
print(students > chemistry_students) # True
print(students > mathematics_students) # False

# Subset
print(physics_students < students) # True
print(chemistry_students < students) # True
print(students == mathematics_students) # True
print(students > mathematics_students) # False Same elements have equal elements.

# You can count the items in a set with the len() global function:
print(len(students)) # 5

# You can get a list from the items in a set by passing the set to the list() constructor.
# Eliminate duplicates from a list. List allows duplicate values but set does not allow duplicate values.
card_list = {1,1,1,2,3,4,5,6,7,8,9,9,8,7,2}
print(list(set(card_list))) # Duplicates have been eliminated.

# In Operator : You can check if an item is contained into a set with the in operator.
print(1 in card_list) # True
print(33 in card_list) # false