decimais = [0,1,2,3,4,5,6,7,8,9]
octal = [0,1,2,3,4,5,6,7]
hexadecimal = [0 ,1 , 2,3 ,4 ,5 ,6 ,7 ,8 ,9 ,'a','b','c','d','e','f']
binario = [0,1]

sistemas_numericos = [decimais, octal, hexadecimal, binario]


n = int(input('Digite um valor em decimal:'))
bina = str(bin(n))
octal = str(oct(n))
hexa = str(hex(n))

respostas = [bina, octal, hexa]
respostas_finais = []

for key in respostas:
	x= 0
	resp = ''
	for letra in key:
		x += 1
		if x > 2:
			resp += f'{letra}'
	respostas_finais.append(resp)




print(f'''
	seu numero em decimal foi {n}
	seu numero em octal foi {respostas_finais[1]}
	seu numero em hex foi {respostas_finais[2]}
	seu numero em binario foi {respostas_finais[0]}
''')
