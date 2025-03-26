#if eles statement
if True:
    pass
else:
    pass


#if elif statement
if True:
    pass
elif False:
    pass
elif 1==2:
    pass
else:
    pass


#for loops with string statement
print("for loops with string statement")
for i in "abcdefg":
    print(i)
print("")


#for loops with range statement
print("for loops with range statement")
for j in range(10):
    print(j)
print("")


for j in range(0, 10):
    print(j)
print("")


for j in range(0, 10, 2):
    print(j)
print("")


#while loops statement
print("while loops statement")
x = 8
c = 0
while True:
    if c >= x:
        break
    print(c)
    c = c + 1
print("")

while c < x:
    print(c)
    c += 1