import random

arr1=[1,2,3,4,5]
i=len(arr1)-1
for x in range(i):
    random_index=random.randint(0,i)
    var = arr1.pop(random_index)
    arr1.append(var)
print(arr1)


def skyline(arr2):
    top=0
    for t in range(len(arr2)):
        if (arr2[t] > top):
            top=arr2[t]
            print(top)
    return(top)
skyline([-1,1,1,7,3])

array1=[4,15,100]
array2=[10,20,30,40]
array3= array1+array2

for i in range(0,len(array3)):
    for a in range (i+1,len(array3)):
        if(array3[i]>array3[a]):
            array3[i],array3[a]=array3[a],array3[i]
print(array3)