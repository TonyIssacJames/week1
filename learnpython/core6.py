import functools
b=[1,2,3,4,5,6,]
f=lambda a,x: a if (a>x) else x
print(functools.reduce(f,b))