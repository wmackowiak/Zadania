#Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
#
# list = input("Podaj listę liczb całkowitych")
# list = list.split(",")
# if list[0] == list[-1]:
#     print("są takie same")
# else:
#     print("Nie są")

numbers = int(input("Ile liczb chcesz dodać? "))

my_numbers=[]
for num in range(numbers):
    num = float(input("Podaj listę liczb "))
    my_numbers.append(num)

print(my_numbers)
if my_numbers[0] == my_numbers[-1]:
    print("Są takie same")
else:
    print("Nie są takie same")






