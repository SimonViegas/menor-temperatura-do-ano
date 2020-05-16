import random

dias = 365
# dias = 5
temperatura = 0
temperturaMenor = 999
diaMenor = 0

for dia in range(1, dias+1):
  # temperatura = int(input('Informe as temperatura do dia: '))
  print('Informe a temperatura do dia', dia, ':', end = '')
  temperatura = random.randint(18, 33)
  print(temperatura)
  
  if temperatura < temperturaMenor:
    temperturaMenor = temperatura
    diaMenor = dia

print('\nA media de temperatura do ano foi --> ', temperturaMenor)
print('Ocorreu no dia', diaMenor)
