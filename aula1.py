import math


a = float(input('Qual é o tamanho do cateto 1 :'))
b = float(input('Qual é o tamanho do cateto 2 :'))

a = a**2
b = b**2

c = math.sqrt(a+b)

print('A sua hipotenuza é igual a {}'.format(c))







if a < b:
	print('Cateto 2 é maior que o cateto 1')
	print('Q catetao gostozo')
	print('say hellow')

elif a == b:
	print('Eles são iguais') 

else:
	print('Cateto 1 é maior que o cateto 2')
	print('Esse nao é tao gostozo')

print('ola mundo')

