import random

tupla = (0,1,2,3,4,5,6,7)#tupla()
lista = []#list() 
dictionary = {}#dict()

for i in range(0,100):
	level = int(random.random()*100)
	hora = int(random.random()*10)
	rank = int(random.random()*100)
	dictionary[f'player{int(random.random()*1000000000)}'] = [i, level,hora,rank]

for i in dictionary:
	print(f'''
				     [INFO]	
		ID: {i}
		RANK: {dictionary[i][0]}
		LEVEL : {int(random.random()*100)}
		HORAS : {int(random.random()*10)}
		''')

a = None


def menu_options_new():
	user_options = input(''' 
		Opçao 1 - Registrar : 1
		Opçao 2 - Sair : 2

		exec:''')
	if user_options == '1':
		user = input('username :')
		date = input('data de nacimento :')
		email = input('email :')

		for i in dictionary:
			rank = dictionary[i][0]
		rank = int(rank)+1

		a = f'player{int(random.random()*1000000000)}'
		dictionary[a] = [rank,0,0,0,user, date, email]
		print("voçe foi cadastrado")
	
	elif user_options == '2':
		exit()




while True:
	if a == None:
		menu_options_new()
	else:
		menu_options_new()