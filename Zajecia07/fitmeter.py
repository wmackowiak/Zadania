import bmi

# podaj wagę i wrost
weight = float(input("Podaj wagę w kg: "))
height = float(input("Podaj wzrost w m: "))

# wyślij wagę i wzrost do funkcji obliczjącej
result_bmi = bmi.calculate_bmi(weight, height)
state = bmi.get_state(result_bmi)
print(state)

filename = state.lower() + '.txt'
with open(filename) as fopen:
        tip = fopen.read()
print(tip)
