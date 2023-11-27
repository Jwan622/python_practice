'''
A function in python can have multiple statements, while loop, if-else statement, and other programming constructs to perform any task. On the other hand, a lambda function can have only one statement.

We define a lambda function using the lambda keyword in python. The syntax for declaring a lambda function is as follows.

myFunction = lambda [arguments]: expression
'''

square = lambda m, n: n ** 2 + m
print("Square of 4 is: ", square(4, 3))


a = 10
b = 20
some_l = (lambda: a, lambda a: b)[1](2)
print('some l', some_l)

# some tuple stuff
t = (1,2,3)[0]
print('tuple t:', t)

test_list = [1,2,3]
print('does this int(str) work?', str(test_list))
