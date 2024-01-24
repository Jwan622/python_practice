test_str = 'test'
result = test_str.center(20, '-')
print('result: ', result)

test_str = 'this will be split'
result = test_str.split()
print('result: ', result)

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

txt = "CompanyX"
x = txt.isalpha()
print(x)

txt = "Demo"
x = txt.isidentifier()
print(x)

txt = "50800"
x = txt.isdigit()
print(x)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
