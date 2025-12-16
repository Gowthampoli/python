#group of elements/values/items/objects as one entry
#allowed duplicates & hetrogeneous elements

a=()
b=10,20
c=(10,20,30.5,True,"Rahul",[],(),{})
enames=("RG","SG","PG","Modi")
print(a)
print(b)
print(c)
print(enames)
print('-------------')
print(type(a))
print(type(b))
print(type(c))
print(type(enames))
print('-------------')
print(enames[0])
print(enames[1])
print(enames[2])
print(enames[3])
print('-------------')
print(enames[-1])
#print(enames[8]) #IndexError: tuple index out of range

enames[0]="Rahul" #TypeError: 'tuple' object does not support item assignment
print(enames)



