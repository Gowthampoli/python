a=10
b=20
c=30.5
d="40"
e="Rahul"
f="Gandhi"
g=True
h=False

print(a+b)
print(a+c)
# print(a+d) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a+e) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(d+f)
print(e+f)
# print(e+g) # TypeError: can only concatenate str (not "bool") to str
print(a+g)
print(a+h)
print(g+h)