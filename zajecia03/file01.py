f = open('zen.txt', mode='r')

print(next(f))
print(next(f))
print(next(f))
print(list(f))

print(next(f))  # StopIteration
