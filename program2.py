import program3

str="Hello World!"
print(str)

def func1():
    print('In func1')
print('Outside func1')

def func2():
    return 'In fumc2'

func1()

str2=func2()

print(str2)