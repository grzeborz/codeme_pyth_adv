f = open('zen.txt', mode='r')

# content = list(f)
content = f.readlines()

# Obie powyższe linijki robią to samo.
# Obie jednak nie zadziałają razem. Każda wysyca iterator.

print(content)

# Z danych w zmiennej `content` możemy skorzystać wielokrotnie.
