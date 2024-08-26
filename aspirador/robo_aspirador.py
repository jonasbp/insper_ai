import numpy as np
from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class RoboAspirador(State):

    def __init__(self,op,posicao_robo,mapa):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = posicao_robo
        self.mapa = mapa

    
    def successors(self):
        # O que ele pode fazer dentro do mapa
        successors = []
        # Pode ir para CIMA,BAIXO,DIREITA,ESQUERDA
        nova_posicao = (posicao_robo[0] - 1, posicao_robo[1])
        successors.append('Mover para cima',nova_posicao,mapa)

        

        return successors
    
    def is_goal(self):
        # Fazer
    
    def description(self):
        return "Robo simples limpador de chão"
    
    def cost(self):
        return 1
    
    def env(self):
        None
        
def main():
    print('Busca em profundidade iterativa')
    # 0 - SUJO | 1 - LIMPO
    state = RoboAspirador('',(0,0),np.array[[1,1],[1,1]])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()