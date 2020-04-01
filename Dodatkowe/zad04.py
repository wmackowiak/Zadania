# Proszę utworzyć ciąg z listy utworzonej za pomocą funkcji range() tak żeby wyświetlić ciąg liczb tylko do wartości 5.
# Moja lisa: [1, 2, 3, 4, 5, 6, 7, 8]

a = list(range(1,9))
print("Moja lista: ",a)
for b in a:
    if b ==5:
        break
    print(b)