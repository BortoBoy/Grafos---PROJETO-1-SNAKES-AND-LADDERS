#Funções para calculo do Power Method
import numpy as np

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

def PoweredPValidator(pP):
	vetor = np.zeros([1,36], float)
	for line in range(0, pP.shape[0]):
		for collum in range(0, pP.shape[1]):
			vetor[0][line] += pP[line][collum]
	print('Validation:' + str(vetor))

