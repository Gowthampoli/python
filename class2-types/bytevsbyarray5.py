ba = bytearray([10,20,30,255,40])
print(type(ba))
ba[0] = 11
print(ba)
for value in ba:
    print(value)


b=bytes([10,20,30,255,40])
print(type(b))
b[0]=11