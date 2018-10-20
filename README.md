# Grafos---PROJETO-1-SNAKES-AND-LADDERS
Um dos 5 trabalhos finais de grafos

Snakes and Ladders é um famoso jogo de tabuleiro em que a cada rodada um jogador joga uma moeda não viciada e avança 1 casa se obtiver cara ou avança 2 casas se obtiver coroa. Se o jogador para no pé da escada, então ele imediatamente sobe para o topo da escada. Se o jogador cai na boca de um cobra então ele imediatamente escorrega para o rabo. O jogador sempre inicia no quadrado de número 1. O jogo termina quando ele atinge o quadrado de número 36.

Com base nas informações, responda:

#a)Especifique a matriz de transição de estados P que define a função de transição da cadeia de Markov Homogênea.

A matriz foi criada com base na imagem inserida na descrição do trabalho. Foram criados duas listas, uma para as cobras(snakes) e outra para escadas (leaders). Tais listas possuem tuplas bidimencionais onde o primeiro elemento é o começo do atalho (base da escada ou cabeça da cobra) e o segundo elemento é a o final (topo da escada ou rabo da cobra).

	_leaders = [(2,15),(5,7),(9,27),(18,29),(25,35)]
	_snakes = [(17,4),(24,16),(20,6),(34,12),(32,30)]

A partir desses vetores a função PSpawer foi criada, retornando a P como matriz de probabilidades. As probabilidades entre os estados foram dispostas segundo o seguinte grafo:

	Grafo do jogo

Gerando a matriz P através da função PSpawer:

	PSpawer

Essa função gera uma matriz quadrada de dimensão igual ao número de estados. O primeiro looping incrementa x até o numero de linhas, procurando na lista de snakes and leaders alguma tupla que tenha x+1 ou x+2 na primeira posição, se for encontrada ele salva o valor do segundo elemento da tupla na variável destiny, que é uma tupla de duas posições, a primeira posição salva o valor encontrado em x+1 e a segunda posição salva para o valor encontrado em x+2. Depois de sair do looping, destiny contém os valores de jump (snakes ou lead), quando não há nenhum jump o padrão em destiny é -1. Esse mesmo looping aproveita para setar uma flag que diz se essa linha esta zerada. Saindo do looping entramos nas condições, são elas:
	- Se as a flag line_zeros estiver setada não faça nada
	- Se não:
		- Verifica se a primeira posição de destiny é -1, se for então não existe jump em x+1 e x+1 pode ser setado para 0.5, pois é a chance da moeda cair cara.
		- Se não for -1 então há um jump, e o valor o elemento com a posição igual ao valor da segunda posição de destiny será setado para 0.5.		
		- Essas duas ultimas verificações se repetem para x+2, e tanto em x+1 quanto em x+2 são feitas correções para o limite do numero de estados, isso é, quando x for igual n-1 (sendo n o número de estados/casas do jogo), então x+1 deve ser setado em 1 ao invés de 0.5, pois não existe x+2 no jogo, à menos que haja um jump em x+1. A mesma verificação é feita para x+2.
	
	[[0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.5 0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.5 0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.5 0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.5 0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1. ]
	 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1. ]]

Cada linha da tabela corresponde à uma casa, e cada valor na linha corresponde à probabilidade de ir para o estado referente a coluna na próxima jogada. Assim, casas que possuem começo de atalhos possuem linhas zeradas (soma dos elementos da linha igual a zero), pois o jogador nunca estará nesse estado, sempre será levado para o final do atalho. Da mesma forma, nenhuma das outras linhas pode ter probabilidade de saltar para um estado zerado, isso é, se a linha x é zerada, a coluna x também é, pois nenhuma linha pode saltar para este estado.

#b)Desenvolva um script em Python para calcular a distribuição estacionária da cadeia de Markov homogênea em questão. Qual é a probabilidade de um jogador vencer o jogo, ou seja, qual a probabilidade de se atingir o estado 36 no longo prazo? Considere k = 100 um número suficiente de iterações no Power Method. Qual o estados mais provável de ser acessado? (Lembre-se que que o último estado, 36, é absorvente, ou seja, uma vez atingido não há saída)

Aṕos gerar a tabela em a) foram implementadas funções para validar esta mesma, visto que, como pode possuir um numero muito grande de de entradas, nesse caso 36^2 = 1296, está sucetpivel à muitos erros. As funções foram criadas para verificar propriedades da tabela, como linhas e colunas zeradas e printar as transições para melhor visualização das snakes and leaders.

	PValidator

Foi implementada a função para calcular a multiplicação de matrizes

	MultMatrix

Em seguida foi criado o método pricipal do problema, que realiza o Power Method para calcular a distribuição estacionária. Multiplicando a matriz P por ela mesma em um looping de k repetições, que é equivalente à elevar P em k (P^k).

	PowerMethod

Um método para validação da matriz elevada também foi implementado, para verificar se a soma de cada linha é igual a 1. Esses métodos de validação foram muito importantes na hora de verificar os erros inseridos na matriz.

	PoweredPValidator

A distribuição estacionária encontrada para 100 iterações foi como esperada:

	w0 para 100

O ultimo estado, 36, está muito próximo de 1 e todos os outros muito próximos de 0.


#c) Especifique a matriz P_ (P_barra) referente ao modelo Pagerank considerando alpha = 0.1. Considerando k = 100, aplique o Power method e compare o resultado com o obtido no item b). As distribuições estacionárias obtidas em b) e c) são iguais ou diferentes?

A matriz P_ foi especificada usando a função PBarraSpawer que se encontra no arquibo pagerank.py, junot com ela há também um método que printa a soma de cada linha, para verificar a validação desta.

	PBarraSpawer

A matriz Pbarra é gerada e logo depois sua distribuição estacionária é calculada. Com as funções já implementadas descritas acima. É possível notar que, para:

	- k = 100
	- k = 200
	- k = 1000






