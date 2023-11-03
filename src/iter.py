customers = ['Alice', 'Bob', 'Carl', 'Dave', 'Elena', 'Frank']
iterator = iter(customers)
print(next(iterator))
print(next(iterator))
for x in iterator:
    print(x)


class Data:
    def __init__(self, data):
        self.data = data # an iterable

    def __iter__(self):
        print('in iter')
        self.current_index = 0
        return self

    def __next__(self):
        print('in next')
        if self.current_index < len(self.data):
            x = self.data[self.current_index]
            self.current_index += 1
            return x
        raise StopIteration

'''
iter calls the internal __iter__ method and the next function internally calls teh __next__ function
'''

# d = Data([1, 'Alice', 42, 'finxter'])
# # Create an iterator
# iterator = iter(d)
# # Dynamically generate the next values - iterate!
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

from itertools import count

# create an infinite iterator that starts at 3 and increments by 1 each time
infinite_iterator = count(3)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))


