print("Non Sequences")
#int
q = 10
print(type(q))
#complex
a = 3 + 4j
print(a)
print(type(a))
b = 5j
print(type(b))
print(b)
#bool
c = True
print(type(c))

d = None
print(type(d))


print("Sequences")
#List
a = [1, 2, 3, 4]
print(a)
print(type(a))
#Tuple
b = (1, 2, 5, 6)
print(b)
print(type(b))
#here paranthesis are optional
b = 1, 2, 5, 6
print(type(b))

# if one element in tuple use comma otherwise it considers as a integer
a = 1
print(type(a))
a = 1,
print(type(a))
#set
c = {1, 3, 5}
print(type(c))
#frozenset
f = frozenset({1, 2, 4})
print(type(f))
#dict
e = {'1': 'apple', '2': 'cherry', '3': 'mango'}
print(e)
print(type(e))

r1 = range(1, 10, 2)
print(*r1)

r2 = range(10, 1, -3)
print(*r2)

a = list(range(10, 2, -2))
print(a)

print("Type Conversion")
g = dict([['a', 1], ['b', 1], ['c', 1]])
print(g)

a = 1, 2, 3, 4
a = list(a)
print(a)