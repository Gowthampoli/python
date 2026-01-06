numbers=[1,2,3,4,5,6,7,8,9,10]
def even_no(num):
    return num%2==0

print(list(filter(even_no,numbers)))
print('-'*20)


print(list(filter(lambda num:num%2==0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])))
