from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class RoboAspirador(State):

    def __init__(self, op,posicao_robo, situacao_esq, situacao_dir):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = posicao_robo
        self.situacao_esq = situacao_esq
        self.situacao_dir = situacao_dir
    
    def successors(self):
        successors = []
        # Unica ação é mover o robo para a esquerda - Resto igual portanto pega do self
        # IR PARA A ESQUERDA - CONSEQUÊNCIA
        successors.append(RoboAspirador('Ir para a esquerda','ESQ',self.situacao_esq,self.situacao_dir))

        # IR PARA A DIREITRA
        successors.append(RoboAspirador('Ir para a direita','DIR',self.situacao_esq,self.situacao_dir))

        # LIMPAR
        # LIMPAR A ESQUERDA
        if self.posicao_robo == 'ESQ':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,'LIMPO',self.situacao_dir))
        # LIMPAR A DIREITA
        if self.posicao_robo == 'DIR':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,self.situacao_esq,'LIMPO'))

        return successors
    
    def is_goal(self):
        return self.situacao_esq == 'LIMPO' and self.situacao_dir == 'LIMPO' 
    
    def description(self):
        return "Robo simples limpador de chão"
    
    def cost(self):
        return 1
    
    def env(self):
        None
        
def main():
    print('Busca em profundidade iterativa')
    # Estado inicial do robô
    state = RoboAspirador('',"DIR", "SUJO", "SUJO")
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()