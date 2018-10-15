file = open('P.txt', 'w')
leaders = [(2,15),(5,7),(9,27),(18,29),(25,35)]
snakes = [(17,4),(24,16),(20,6),(34,12),(32,30)]
_x = 6
_y = 6
_n = _x * _y

#header
file.write('     ')
for i in range(1, _n+1):
		file.write(str(i) + '    'if(i<10) else str(i) +'   ')
file.write('\n')


#body
jump = -1
for line in range(1, _n+1):		
	file.write((' ' if(line<10) else '') + str(line) + '|')	#sider	
	for tupla in leaders+snakes:	#procurando cobras ou escadas conectadas
		if(line == tupla[0]):
			jump = tupla[1]
			break
	
	for collum in range(1, _n+1):
		if(jump == -1):
			file.write(' 1/2 'if(collum == line+1 or collum == line+2) else '  0  ')
		else:
			file.write('  1  'if(collum == jump)else '  0  ')
	jump = -1
	file.write('|\n')



	
