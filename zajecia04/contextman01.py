with open('zen.txt', mode='r') as file:
    contents = list(file)
    print(contents)
    print('zamknięty?', file.closed)

print('zamknięty?', file.closed)  # obiekt 'file' jest nadal dostępny poza context managerem
