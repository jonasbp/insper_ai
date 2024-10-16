from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import numpy as np

class AspiradorPo2(State):

    def __init__(self, op, matriz_casa, posicao_aspirador):
        #Necessário utilizar op como o nome do operador;
        self.operator = op

        #Qual a situação da casa?
        # [[X, X]
        #  [X, X]]
        #0 = sujo;
        #1 = limpo;
        self.matriz_casa = matriz_casa

        #Onde o aspirador está?
        # (X, Y)
        self.posicao_aspirador = posicao_aspirador

    
    def successors(self):
        #Retorna todos os estados filhos possíveis;
        #Lista de instâncias (objetos) do tipo AspiradorPo;
        #Para cada ação (operador), vamos ter um estado filho - uma instância do objeto;
        successors = []

        #Move o aspirador para a esquerda;
        if self.posicao_aspirador[1] > 0:
            nova_posicao = (self.posicao_aspirador[0], self.posicao_aspirador[1] - 1)
            s1 = AspiradorPo2('mover_esq', self.matriz_casa, nova_posicao)
            successors.append(s1)
        
        #Move o aspirador para a direita;
        if self.posicao_aspirador[1] < (self.matriz_casa.shape[1]-1):
            nova_posicao = (self.posicao_aspirador[0], self.posicao_aspirador[1] + 1)
            s2 = AspiradorPo2('mover_dir', self.matriz_casa, nova_posicao)
            successors.append(s2)
        
        #Move o aspirador para cima;
        if self.posicao_aspirador[0] > 0:
            nova_posicao = (self.posicao_aspirador[0] - 1, self.posicao_aspirador[1])
            s3 = AspiradorPo2('mover_cima', self.matriz_casa, nova_posicao)
            successors.append(s3)
        
        #Move o aspirador para baixo;
        if self.posicao_aspirador[0] < (self.matriz_casa.shape[0]-1):
            nova_posicao = (self.posicao_aspirador[0] + 1, self.posicao_aspirador[1])
            s4 = AspiradorPo2('mover_baixo', self.matriz_casa, nova_posicao)
            successors.append(s4)

        #Limpa o quarto;
        if self.matriz_casa[self.posicao_aspirador[0], self.posicao_aspirador[1]] == 0:
            nova_matriz_casa = np.copy(self.matriz_casa)
            nova_matriz_casa[self.posicao_aspirador[0], self.posicao_aspirador[1]] = 1  
            s5 = AspiradorPo2('limpar', nova_matriz_casa, self.posicao_aspirador)
            successors.append(s5)

        return successors
    
    def is_goal(self):
        #Retorna True se o estado atual é um estado objetivo;
        return np.all(self.matriz_casa == 1)
    
    def description(self):
        return "Problema do Aspirador de Pó"
    
    def cost(self):
        #Retorna o custo para alcançar este estado, sendo que cada estado pode ter um custo diferente;
        return 1 #Problema de custo uniforme;
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None

def main():
    print('Busca em largura para o problema do Aspirador de Pó')
    state = AspiradorPo2('', np.array([[1, 1, 1], 
                                       [1, 1, 0]]), (0, 0)) 
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Não achou solução')

if __name__ == '__main__':
    main()