# iterate through variable array backwards
some_var1 = ['a', 'b', 'c', 'd', 'e']
for index in range(len(some_var1) - 1, 0, -1):
  print(some_var1[index])

# let's see what x range does
some_var2 = 'some_string'
print(some_var2[0:6])
print(some_var2[:3])  # first 3 elements
print(some_var2[-3:])  # first 3 elements
print(some_var2[0:6:1])
print(some_var2[0:6:2])
print(some_var2[1:6:2])
print(some_var2[::2])  # the last number is step
print(some_var2[::-1])

# if original input is a string all 3 return same result
some_var3 = 'hi there I am a string'


def reverse(text):
  result = ""

  for i in range(len(text), 0, -1):
    result += text[i - 1]

  return result


print('method reverse:', reverse(some_var3))
print('slice operator: list_name[start:end:step]: ', some_var3[::-1])
print('using reversed built in: ', "".join(reversed(some_var3)))

