# create
l1=[]
l2=list()
eids=[101,102,103,104]
elements=[10,20,20.5,'Hello',True,10]
numbers=[10,20,10,30,40,20,20]
a=[1,2,3]
b=['a','b','c']


# read
print(eids[2])
print(elements[1:5])
print(numbers[-3:]) 
print(elements[:])
print(numbers.count(20))
print(numbers.index(30))
print(len(elements))
print('-------------')

# update
print(elements)
elements[3]='World'
print(elements)
elements.pop()
print(elements)
print('*')

print(eids)
eids.append(500)
print(eids)
print('*')

print(numbers)
numbers.insert(1,10.5)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print('*')

print(a)
print(b)
a.extend(b)
print(a)
print('-------------')


# delete
print(elements)
elements.remove(20.5)
print(elements)
del elements[1]
print(elements)
elements.clear()
print(elements)
print(len(elements))
print('-------------')

enames=['Rahul', 'sonia', 'Priyanka', 'Modi', 'Amit']
i=0
while i<=len(enames)-1:
    print(enames[i])
    i=i+1



