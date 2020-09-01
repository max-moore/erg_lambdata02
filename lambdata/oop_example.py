

import pandas as pd
# you can make children of class you didn't write
# as an excersize try to use or build on this!


class ErgDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]


class BareMininumClass:
    pass


class Complex:
    def __init__(self):  # constuctor - special function that creates instance of class
        """
        Complex numbers are part real, part imaginary.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.imaginary

    def __repr__(self):  # returns a string
        return '({}, {})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def recieve_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """ General Representation of animals.""""

    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return "Vroom!"

    def eat(self, food):
        return food + " is delicious, yum!"


class Tiger(Animal):
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)

    def say_great(self):
        return "It's GREEEAAAAT"

    def run(self):
        # Overriding run
        return "Scamperwoosh!"

    pass


if __name__ == "__main__":
    # Demo code if you run `python oop_examples.py`
    # Example 0
    b = BareMinimumClass()
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2)  # What should num1 be after?
    print(num1.r, num1.i)
    # Example 2
    user1 = SocialMediaUser('erle', 'Jax')
    user2 = SocialMediaUser('John', 'New York', upvotes=50)
    user3 = SocialMediaUser('John Doe', 'Anytown, USA')
    print(user2.is_popular())  # False
    for _ in range(75):
        user2.receive_upvote()
    print(user2.is_popular())  # True
