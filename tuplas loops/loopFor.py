import time

cadena = 'Python'

for letra in cadena:
   if letra == 'o':
      continue
   print(letra)
   time.sleep(1)