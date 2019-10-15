x = True
foo = ['bar', 12345, x]
print(foo[2])
bar = foo[:]
print(bar)
foo[2] = 1
print(bar[2])
print(34 in foo)
print(foo.index(x))

a = ['bar']
for test in 'bar':
    print(test)
