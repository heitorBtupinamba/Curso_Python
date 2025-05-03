#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informações possíveis sobre ele.

entrada=input("Digite algo: ")
print()

print('O tipo primitivo do que foi digitado é:',(type(entrada)))

print('Só tem espaços?:',entrada.isspace())

print('É um número?:',entrada.isnumeric())

print('É alfabético?:',entrada.isalpha())

print('É alfanumérico?:',entrada.isalnum())

print('Está em maiúsculo?:',entrada.isupper())

print('Está em minúsculo?:',entrada.islower())

print('Está capitalizada?:',entrada.istitle())
