# Object Oriented Programming
# building a class Set() that mimicks the inbuild Python class set()
class Set():

    # these are the member functions
    # every one takes a first parameter "self" (another convention)
    # that refers to the Particular Set object being used.

    def __init__(self, values=None):
        """
        This is the constructor,
        It gets called when you create a new Set.
        You would use it like
        s1 = Set()  # empty set
        s2 = Set([1,2,2,3])  # initialize with values
        """

        self.dict = {}  # each instance of Set has its own dict property
        # which is what we'll use to track memberships
        if values is not None:
            for value in values:
                self.add(value)

    # We'll represent membership by being a key in self.dict with value True.
    def add(self, value):
        self.dict[value] = True

    # value is in the set if it's a key in the directory
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

    def __repr__(self):
        '''
        this is the string representation of a Set object
        if you type it at the Python prompt or pass it to str()
        '''
        return print("Set: " + str(self.dict.keys()))


set_obj = Set([2, 3, 4, 5])
print(set_obj)
set_obj.remove(3)
set_obj.add(3)
set_obj.contains(3)