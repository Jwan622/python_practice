xs = ["word1", "word2", "word3"]

print('capitalized words:', [x.capitalize() if x is not None else '' for x in xs])
'''
Its structure consists of: "brackets containing an expression followed by a for clause, then zero or more for or if clauses".
'''

forward_range = [x for x in range(1, 10, 2)]
print('forward range skip by 2', forward_range)

backward_range = [x for x in range(10, -1, -2)]
print('backward range skip by 2', backward_range)

even_range = [x for x in range(1, 11) if x % 2 == 0]
print('even range', even_range)

# lsit comprehension with conditionals
new_list = ['even' if x % 2 == 0 else 'number three' if x == 3 else 'odd' for x in range(1, 10)]
print('two condition list comprehension', new_list)

'''
1 if A else 2 if B else 3 translates to this:

def myexpr(A, B):
    if A:
        return 1
    else:
        if B:
            return 2
        else:
            return 3
'''

age = 25
category = "adult" if age >= 18 else "minor"
print('category', category)

'''
Assuming we opted to use an if-else statement instead of a Python ternary operator, it would look something like this:
age = 25

if age > 18:
   category = "Adult"
else:
   category = "Minor"
'''

c = False
result = ('a', 'b')[c]


# lambda
a = 10
b = 20
max_value = (lambda: a, lambda: b)[True]()
print('lambd amax value:', max_value)


'''
age = 21

#Normal elif statement
if age< 21:
   print('Child')
elif age< 25:
   print ('young adult')
else:
   print('Adult')

#elif statement as a ternary operator
print('Child') if age < 18 else print('Young adult') if age <21 else print ('Old Person')

#Output: 'Young Adult'
'''
age = 20
color = 'bluez'
print('Child') if age < 18 else print('Young adult') if age < 21 and color == 'red' else print ('Old Person') if color == 'blue' else print ('hi')