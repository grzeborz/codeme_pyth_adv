file = open('zen.txt', mode='r')
contents = list(file)
print(contents)
print('zamknięty?', file.closed)

file.close()

print('zamknięty?', file.closed)
