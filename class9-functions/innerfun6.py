def outer():
    print("outer function")
    
    def inner():
        print("inner function invoked from outside")

    def inner2():
        return "inner2 function invoked from outside"
    
    return inner, inner2

inner, inner2 = outer()
inner()

print(inner2())

print('-'*20)
