#create
d1={}
emp={'eid':101,'ename':'Rahul','esal':45000.45}
user={'uid':101,'uname':'Sonia','loc':'Delhi','loc':'Ap'}

#read
print(d1)
print(emp)
print(user)
print('----------')

print(type(d1))
print(type(emp))
print(type(user))
print('----------')

print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(user['loc'])
print('----------')

#update
emp['ename']='Rahul Gandhi'
print(emp)
print('----------')

#delete
del emp['esal']
print(emp)
print('----------')




