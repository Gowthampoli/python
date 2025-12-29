s1={}
s2=set()
s3={10,20,30}
s4=set([10,20,30,'Hello',True,10.5])
enames={'Alice','Bob','Charlie','David'}
eids={101,102,103,104,105}

# read
print(s3)
print(s4)
print(type(s1)) 
print(type(s2))
print(type(s4))
print(len(s4))
print('-------------')

# update
print(s4)
s4.add('World')
print(s4)
s4.update([100,200,300])
print(s4)
s4.pop()  # Removes and returns an arbitrary element
print(s4)
print('-------------')

# delete
print(s3)
s3.clear()
print(s3)
print(len(s3))
s4.discard(800)  # Does not raise an error if element not found
s4.discard('Hello')
print(s4)
s4.remove(10)
print(s4)
print('-------------')

enames={'Rahul', 'sonia', 'Priyanka', 'Modi'}
i=0
for name in enames:
    print(name)
    i=i+1

print('Total names:', i)
