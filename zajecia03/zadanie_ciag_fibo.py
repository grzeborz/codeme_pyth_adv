# Stwórz funckję fibo(), która zwróci generator kolejnych liczb ciągu Fibonacciego.
# # Aby przetestować funkcę, w bloku if main wygeneruj dziesięć pierwszych liczb Fibonacciego i porównaj je z ciągiem powyżej.

def fibo():
    n = 0
    m = 1
    yield n
    yield m
    while True:
        w = n + m
        yield w
        n = m
        m = w



if __name__ == '__main__':
    f = fibo()
    for i in range(10):
        print(next(f))
