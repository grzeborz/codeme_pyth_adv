from iter02 import EvenNumbers

numbers = EvenNumbers()

print(next(numbers))
print(next(numbers))
print(numbers.__next__())  # tak też można, ale powyżej jest ładniej

print(list(numbers))

# print(next(numbers))  # to rzuci wyjątek, gdyż nie ma już następnego elementu
