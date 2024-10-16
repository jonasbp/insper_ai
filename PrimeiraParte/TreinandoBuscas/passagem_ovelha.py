from aigyminsper.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.Graph import State
import numpy as np

class passagemOvelha(State):

    def __init__(self, op, lobo, carneiro,alface,homem):
        # ELES PODEM TER "D" ou "E"
        self.operator = op
        self.lobo = lobo
        self.carneiro = carneiro
        self.alface = alface
        self.homem = homem

    
    def successors(self):
        #Retorna todos os estados filhos possíveis;
        #Lista de instâncias (objetos) do tipo AspiradorPo;
        #Para cada ação (operador), vamos ter um estado filho - uma instância do objeto;
        successors = []
        #Ação 1: O homem leva o lobo;
        
        

        return successors
    
    def is_goal(self):
        if self.lobo == 'D' and self.carneiro == 'D' and self.alface == 'D' and self.homem == 'D':
            return True
        return False
    
    def description(self):
        return "Problema do Aspirador de Pó"
    
    def cost(self):
        return 1 
    def env(self):
        None

def main():
    print('Busca em largura para o problema do Aspirador de Pó')
    state = passagemOvelha() 
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Não achou solução')

if __name__ == '__main__':
    main()