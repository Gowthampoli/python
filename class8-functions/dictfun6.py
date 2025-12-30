# create
emp ={'eid' : 101,
'ename' : 'Amit',
'gender' : 'Male',
'esal' : 45000,
'loc' : 'Bangalore'}

""" # read
print(emp['ename'])
print(emp.get('esal'))
print(emp.keys())
print(emp.values())
print(emp.items())
print(len(emp))
print(type(emp))

# update
emp['esal']=50000
print(emp)
emp['gender']='Female'
print(emp)

# delete
emp.pop('esal')
print(emp)
emp.popitem()
print(emp)
del emp['loc']
print(emp)
emp.clear()
print(emp)
del emp # delete the dictionary
# print(emp) """

for key in emp.keys():
    print(key)#key,":",emp.get(key))
print('*'*10)

for value in emp.values():
    print(value)
print('*'*10)

for item in emp.items():
    print(item)

