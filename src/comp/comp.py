# The following list comprehension exercises will make use of the
# defined Human class.
import math
import re


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# a = []
# for classes in humans:
#     if re.search("^[D]", classes.name):
#         a.append(classes.name)
a = [classes.name for classes in humans if re.search("^[D]", classes.name)]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
# b = []
# for classes in humans:
#     if re.search("e$", classes.name):
#         b.append(classes.name)
b = [classes.name for classes in humans if re.search("e$", classes.name)]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# c = []
# for classes in humans:
#     if re.search("^[C-G]", classes.name):
#         c.append(classes.name)
c = [classes.name for classes in humans if re.search("^[C-G]", classes.name)]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
# d = []
# for classes in humans:
#     d.append(classes.age + 10)
d = [(classes.age + 10) for classes in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# e = []
# for classes in humans:
#     e.append(classes.name + "-" + str(classes.age))
e = [(classes.name + "-" + str(classes.age)) for classes in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
# f = []
# for classes in humans:
#     if (classes.age in range(27, 33)):
#         f.append((classes.name, classes.age))
f = [(classes.name, classes.age)
     for classes in humans if (classes.age in range(27, 33))]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# g = []
# for classes in humans:
#     classes.name = Human(classes.name.upper(), classes.age + 5)
#     new_humans = classes.name
#     g.append(new_humans)
g = [Human(classes.name.upper(), classes.age + 5) for classes in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
# h = []
# for classes in humans:
#     h.append(math.sqrt(classes.age))
h = [math.sqrt(classes.age) for classes in humans]
print(h)
