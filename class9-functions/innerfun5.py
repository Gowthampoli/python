def outer():
    print("outer function")

    def inner():
        print("inner function")
    inner()
    inner()

outer()
outer()
# inner() # NameError: name 'inner' is not defined
print('-'*20)


def outer():
    print("outer function")
    
    def inner():
        print("inner function invoked from outside")

    return inner

inner=outer()
inner()
inner()
print('-'*20)

