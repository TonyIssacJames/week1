def is_even_with_return( i ):
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3) 
print(is_even_with_return(3) )

def is_even_without_return( i ):
    print('without return')
    remainder = i % 2

is_even_without_return(3)
print(is_even_without_return(3) )


def is_even( i ):
    remainder = i % 2
    return remainder == 0

print("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")