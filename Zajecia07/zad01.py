def count_A(seq):
    counter = 0
    for l in seq:
        if l.lower() == 'a':
            counter +=1
        return counter

word = 'Abrakadabra'
print(count_A(word))