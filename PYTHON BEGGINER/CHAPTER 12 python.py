# lambda expression (anonymous function)

def add(a,b):
    return a + b

add2 = lambda a,b : a+b
print(add2(2,3))

multiply = lambda a,b : a*b
print(multiply(3,2))

print(add)
print(add2)
print(multiply)

# lambda expression practice

def is_even(a):
    return a%2 == 0

print(is_even(99))            


is_even2 = lambda a : a%2 == 0 
print(is_even2(6))

# def last_char(b):
#     return a[-1]


last_char2 = lambda b : b[-1]
print(last_char2('gaurav'))


# lambda with if, else
def func(s):
    return len(s) > 5
print(func('block'))     

func2 = lambda s : len(s) > 5 
func3 = lambda s : True if len(s) > 5 else False
print(func2('gaurav'))
print(func3('ram`'))
