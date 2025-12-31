a=1000
def login():
    print("login success")

print(type(login))
print(type(a))

login()
print(a)
print('-'*20)



def add():
    print("addition")

add()
# add(10) # TypeError: add() takes 0 positional arguments   
print('-'*20)



def add(a,b):
    print(a+b)
add(10,20)
# add(10,'20') # TypeError: unsupported operand type(s) for -: 'int' and 'str'
add('10','20')
print('-'*20)



def calc(a,b):
    print(a+b)

# print(calc(10,20))
# calc(10) # TypeError: calc() missing 1 required positional argument: 'b'
calc(10,20)
print('-'*20)
