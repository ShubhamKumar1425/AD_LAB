a = 10
b = 20
c = 30
print("Variables created.")
print("Current variables:", dir())

del a
print("After deleting 'p':", dir())

del b
del c
print("After deleting all variables:", dir())
