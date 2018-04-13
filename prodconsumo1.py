import random
TAM = 10
buffer = [0]*TAM
ini = fim = 0
nelem = 0
vazios = TAM

def esta_cheio ():
	return nelem == TAM

def esta_vazio ():
	return nelem == 0

def inserir (valor):
	global fim, buffer, nelem
	if esta_cheio ():
		return False

	buffer[fim] = valor
	fim = (fim +1)%TAM
	nelem +=1
	return True

def remover ():
	global ini, buffer, nelem
	if esta_vazio ():
		return False, -1
				
	valor = buffer[ini]
	ini = (ini+1)%TAM
	nelem -=1
	return True, valor

for i in range (20):
	if not inserir (i):
		print ("Não consegui inserir "+ str(i))
		break
for i in range (20):
	x, y = remover ()
	if x:
		print ("Removi "+str(y))
	else:
		print ("Buffer vazio")

def vaga ():
	return nelem < TAM
def cheio ():
	return nelem > 0
mutex = threading.Lock ()
cv = threading.Condition()
def prod ():
	global mutex cv
	with cv:
		cv.wait_for(vaga)
		valor = random.randrange(100)
		return valor
def consumo ():
	global mutex cv
	with cv:
		cv.wait_for(cheio)
				
		
threads=[]
for i in range (2):
	threads.append(threading.Thread(target=prod, args=(i,)))
	threads[-1].start ()
for i in range (2):
	threads[i].join ()

threads=[]
for i in range (2):
	threads.append(threading.Thread(target=consumo, args=(i,)))
	threads[-1].start ()
for i in range (2):
	threads[i].join ()

