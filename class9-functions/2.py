def sub(a,b):
    print(a-b)

sub(10,20)
sub(20,10)
# sub(10,20,30) # TypeError: sub() takes 2 positional arguments but 3 were given
print('-'*20)


def sub(a,b):
    print(a-b)
sub(a=10,b=20)
sub(b=20,a=10)
# sub(10,20,30) # TypeError: sub() takes 2 positional arguments but 3 were given
print('-'*20)


def sub(a,b,c=100):
    print(a-b+c)
sub(20,10)
sub(b=20,a=10)
sub(10,20,30)
print('-'*20)

