eids=[101,102,103,104,105]
print(101 in eids)
print(106 in eids)
print(106 not in eids)
print(105 not in eids)
print('1--------------')

enames=('RG','SG','PG')
print('RG' in enames)
print('SG' not in enames)
print('JG' not in enames)
print('2--------------')

sizes={'S','M','L','XL','XXL'}
print('S' in sizes)
print('XL' not in sizes)
print('XS' in sizes)
print('3--------------')

ename='Rahul'
print('R' in ename)
print('H' not in ename)
print('L' in ename)
print('l' in ename)
print('4--------------')

b=bytes([10,20,30,255])
ba=bytearray([10,20,30,255])
fz=frozenset([10,10,10])
print(10 in b)
print(10 in ba)
print(10 in fz)
print(20 in fz)
print(10 not in ba)
print(10 not in fz)
print('5--------------')

numbers=range(100)
print(50 in numbers)
print(150 in numbers)
print(150 not in numbers)
print('6--------------')