# Esse script calcula a matriz Pbarra (Google MAtrix) referente ao PangeRank
# Pbarra = (1−α) P+α(1/n)U (Google matrix)
import numpy as np

def PBarraSpawer(P, alpha):
	print('Spawing Pbarra')
	Pbarra = ((1-alpha)*P) + alpha/P.shape[0]
	print(Pbarra)
	PbarraValidator(Pbarra)
	return Pbarra

def PbarraValidator(Pbarra):
	vetor = np.zeros([1,36], float)
	for line in range(0, Pbarra.shape[0]):
		for collum in range(0, Pbarra.shape[1]):
			vetor[0][line] += Pbarra[line][collum]
	print('Validation:' + str(vetor))