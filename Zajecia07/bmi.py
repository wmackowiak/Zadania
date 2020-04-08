# funkcja obliczająca bmi <-- waga, wzrost
def calculate_bmi(weight,height):
    return weight/height **2

# funkcja podająca wartość
def get_state(bmi):
    if bmi < 18:
        return "niedowaga"
    elif bmi < 25:
        return "normalna"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otylosc"



