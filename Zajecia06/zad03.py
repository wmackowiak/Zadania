# with open('cytaty.txt', 'r') as f:
#   content = f.read()
#   print(content)

# with open('cytaty.txt', 'r') as fopen:
#   for line in fopen:
#     print(line)

import os
import random

def show_quote(text):
  id = random.randrange(0, 10)
  print('*' * 70)
  print(text[id].strip().center(70))
  print('*' * 70)

filname = input("Podaj nazwę pliku: ")

if os.path.exists(filname) and os.stat(filname).st_size > 0:
  with open(filname, encoding='utf-8') as fopen:
    quotes = fopen.readlines()

  show_quote(quotes)
else:
  print("Brak cytatów")




