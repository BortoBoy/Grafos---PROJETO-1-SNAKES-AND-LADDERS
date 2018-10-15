# Grafos---PROJETO-1-SNAKES-AND-LADDERS
Um dos 5 trabalhos finais de grafos

Snakes and Ladders é um famoso jogo de tabuleiro em que a cada rodada um jogador joga uma moeda não viciada e avança 1 casa se obtiver cara ou avança 2 casas se obtiver coroa. Se o jogador para no pé da escada, então ele imediatamente sobe para o topo da escada. Se o jogador cai na boca de um cobra então ele imediatamente escorrega para o rabo. O jogador sempre inicia no quadrado de número 1. O jogo termina quando ele atinge o quadrado de número 36.

Com base nas informações, responda:


a) Especifique a matriz de transição de estados P que define a função de transição da cadeia de Markov Homogênea.

b) Desenvolva um script em Python para calcular a distribuição estacionária da cadeia de Markov homogênea em questão. Qual é a probabilidade de um jogador vencer o jogo, ou seja, qual a probabilidade de se atingir o estado 36 no longo prazo? Considere k = 100 um número suficiente de iterações no Power Method. Qual o estados mais provável de ser acessado? (Lembre-se que que o último estado, 36, é absorvente, ou seja, uma vez atingido não há saída)

c) Especifique a matriz P_ (P_barra) referente ao modelo Pagerank considerando alpha = 0.1. Considerando k = 100, aplique o Power method e compare o resultado com o obtido no item b). As distribuições estacionárias obtidas em b) e c) são iguais ou diferentes?
