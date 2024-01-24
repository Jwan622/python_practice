'''
This first argument to map() is a transformation function. In other words, it’s the function that transforms each original item into a new (transformed) item. Even though the Python documentation calls this argument function, it can be any Python callable. This includes built-in functions, classes, methods, lambda functions, and user-defined functions.

The operation that map() performs is commonly known as a mapping because it maps every item in an input iterable to a new item in a resulting iterable. To do that, map() applies a transformation function to all the items in the input iterable.
'''
list_of_numbers = [1,3,5]
doubled_list = map(lambda x: x * 2, list_of_numbers)

print(doubled_list)


'''
square() is a transformation function that maps a number to its square value. The call to map() applies square() to all of the values in numbers and returns an iterator that yields square values. Then you call list() on map() to create a list object containing the square values.

Since map() is written in C and is highly optimized, its internal implied loop can be more efficient than a regular Python for loop. This is one advantage of using map().

A second advantage of using map() is related to memory consumption. With a for loop, you need to store the whole list in your system’s memory. With map(), you get items on demand, and only one item is in your system’s memory at a given time.

Note: In Python 2.x, map() returns a list. This behavior changed in Python 3.x. Now, map() returns a map object, which is an iterator that yields items on demand. That’s why you need to call list() to create the desired list object.
'''
def square(number):
	return number ** 2


numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

for ele in squared:
	print('generator on demand for elements', ele)

print(list(squared))


'''
let's use a lambda with map
'''

l = lambda num: num ** 2
squared = map(l, [1,2,3,4,8])
print('list squared with lambda', list(squared))

print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))


string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize, string_it)))
print('is it capitalized', string_it)
print(list(map(str.upper, string_it)))

print(list(map(str.lower, string_it)))

with_dots = ["processing..!", "...strings!", "with!....", "..map..!"]
print(list(map(lambda s: s.strip("."), with_dots)))

# use a list comprehension instead

def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5, 6]


# Using a list comprehension
'''
If you compare both solutions, then you might say that the one that uses the list comprehension is more readable because it reads almost like plain English. Additionally, list comprehensions avoid the need to explicitly call list() on map() to build the final list.
'''
print([square(x) for x in numbers])

# use a generator
gen_exp = (square(x) for x in numbers)
print('using a generator', list(gen_exp))

'''
This code has a main difference from the code in the previous section: you change the square brackets to a pair of parentheses to turn the list comprehension into a generator expression.

Generator expressions are commonly used as arguments in function calls. In this case, you don’t need to use parentheses to create the generator expression because the parentheses that you use to call the function also provide the syntax to build the generator. With this idea, you can get the same result as the above example by calling list() like this:
If you use a generator expression as an argument in a function call, then you don’t need an extra pair of parentheses. The parentheses that you use to call the function provide the syntax to build the generator.


'''