
D=([3,4,5,6,7])
print(D)
D=([3,4,5,6,7])
ch=['hello']
print(D)
D=([3,4,5,6,7])
print(set(ch))
D=([3,4,5,6,7])
M=('madam')
print(D)


D=([3,4,5,6,7])
s=set('M')
print(s)


#elements in frozendata type cannot be modified
S1={10,20,30,40,50}
S2=frozenset(S1)
print(S2)


S3=frozenset('hello everyone')
print(S3)

#set operators
#union operators

set1={1,3,4,6,8,9}
set2={1,67,3,89,9}
z=set1|set2
print(z)
Z1=set1.union(set2)
print(Z1)


a={1,2,3,4}
b={20,40,6,8}
print(a|b)
 

a={1,2,3,4}
b={20,40,6,8}
print(a.union(b))


a={1,2,3,4}
b={20,40,6,8}
print(a.intersection(b))


a={1,2,3,4}
b={20,40,6,8}
print(a.difference(b))


a={1,2,3,4}
b={20,40,6,8}
print(a^b)


a={'red','pink','blue','black'}
b={'voilet','red','black'}
print(a.union(b))


a={'red','pink','blue','black'}
b={'voilet','red','black'}
print(a.intersection(b))

a={'red','pink','blue','black'}
b={'voilet','red','black'}
print(a.difference(b))
a={'red','pink','blue','black'}
b={'voilet','red','black'}
print(a^b)
