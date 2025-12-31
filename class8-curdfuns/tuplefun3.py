# create
t1=()
t2=tuple()
t3=10,20,30
t4=(10,20,30)
t5=(10,20,30,'Hello',True,10.5)
enames=('Alice','Bob','Charlie','David')

# read
print(t3[1])
print(t5[2:5])
print(t5[:])
print(len(t5))
print('-------------')

# update
print(t5)
# Tuples are immutable, so we cannot update them directly.
# However, we can convert to a list, make changes, and convert back to a tuple.
temp_list = list(t5)
temp_list[3] = 'World'
print(type(temp_list))
t5 = tuple(temp_list)
print(t5)
print(type(t5))
# t3[2] = 40  # This will raise an error
# t4.append(40)  # This will also raise an error
print('-------------')

# delete
print(t4)
# Tuples are immutable, so we cannot delete elements directly.
# However, we can convert to a list, remove elements, and convert back to a tuple.
temp_list = list(t4)
temp_list.remove(20)
t4 = tuple(temp_list)
print(t4)
print('-------------')
# Note: We cannot clear a tuple like we do with lists, but we can reassign it to an empty tuple.
t4 = ()
print(t4)
print(len(t4))
print('-------------')


ename=('Rahul', 'sonia', 'Priyanka', 'Modi')
i=0
while i<=len(ename)-1:
    print(ename[i])
    i=i+1