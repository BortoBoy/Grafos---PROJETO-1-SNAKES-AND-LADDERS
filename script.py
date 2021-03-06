import numpy as np
import sys

np.set_printoptions(threshold=np.nan, precision=10, suppress=True, linewidth=500)
_leaders = [(2,15),(5,7),(9,27),(18,29),(25,35)]
_snakes = [(17,4),(24,16),(20,6),(34,12),(32,30)]
w0 = np.zeros([1, 36], int)
if(len(sys.argv) > 1):
	k = int(sys.argv[1])
if(len(sys.argv) > 2):
	w0[0][int(sys.argv[2])] = 1
else:
	w0[0][0] = 1	#default

def PSpawer(_leaders, _snakes, tam):
	_n = tam[0]*tam[1]
	print('spawing P')
	P = np.zeros([36,36], dtype=float)
	for x in range(0, _n):
		destiny = [-1, -1]	#[x+1, x+2]
		line_zeros = False
		
		for tupla in sorted(_leaders+_snakes):	#finding sneakes or _leaders
			if(x == tupla[0]-1):
				line_zeros = True
				break 	#zero's line

			if(x+1 == tupla[0]-1 and destiny[0] == -1):	#finding in x+1
				destiny[0] = tupla[1]
			if(x+2 == tupla[0]-1):	#finding in x+2
				destiny[1] = tupla[1]
			if(tupla[0]-1 > x+2):	#breaking loop to best performance, because the tuples are ordered
				break

		if(not line_zeros):
			if(destiny[0] != -1):
				P[x][destiny[0]-1] = 0.5
			elif(x+1 < _n):
				P[x][x+1] = 0.5
			else:	#i am in the last state
				P[x][x] = 1	

			if(destiny[1] != -1):
				P[x][destiny[1]-1] = 0.5
			elif(x+2 < _n):
				P[x][x+2] = 0.5
			elif(x+1 < _n):
				P[x][x+1] = 1			
	print(P)
	return P

def PValidator(P):
	#printing transitions
	zeros_lines = ()
	for line in range(0,P.shape[0]):
		connections = ()
		for collum in range(0,P.shape[1]):
			if(P[line][collum] != 0):
				connections += tuple([collum])
		if(connections == ()):
			print(str(line + 1) + ': No where')
			zeros_lines += tuple([line])
		else:
			for j in connections:
				print('%d: %d' % (line+1, j+1))
	#verifing errors
	print('verifing zero lines: ' + str(zeros_lines))
	bad_jumper = False
	for line in zeros_lines:
		for j in range(0, P.shape[1]):
			if(P[j][line]):
				print('There is an error on position ( %d , %d )' % (j, line))
				bad_jumper = True
	if(not bad_jumper):
		print('There is no bad jumper')


def PoweredPValidator(pP):
	vetor = np.zeros([1,36], float)
	for line in range(0, pP.shape[0]):
		for collum in range(0, pP.shape[1]):
			vetor[0][line] += pP[line][collum]
	print('Validation:' + str(vetor))

def PowerMethod(w0, P, k):
	print('spawing P^k')
	poweredP = P
	for i in range(0,k):
		poweredP = MultMatrix(poweredP, P)
	print(poweredP)
	print('Validating')
	PoweredPValidator(poweredP)
	print('Calculando distribuicao estacionaria')
	dist = MultMatrix(w0, poweredP)
	print(dist)
	return dist

def MultMatrix(a, b):
	if(a.shape[1] != b.shape[0]):	#no possible result
		raise ArithmeticError ('The first matrix\'s number of colluns must be equal then the second matrix\' number of lines')
	else:
		aXb = np.zeros([a.shape[0], b.shape[1]], int if(a.dtype == int and b.dtype == int)else float)
		for line in range(0, a.shape[0]):
			for collum in range(0, b.shape[1]):
				for jumper in range(b.shape[0]):
					aXb[line][collum] += a[line][jumper]*b[jumper][collum]
		return aXb

P = PSpawer(_leaders, _snakes, [6,6])
PValidator(P)
dist = PowerMethod(w0, P, k)