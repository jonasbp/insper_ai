from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State

class RoboAspirador(State):

    def __init__(self, op,posicao_robo, situacao_esq, situacao_dir,situacao_cima,situacao_baixo):
        # You must use this name for the operator!
        self.operator = op
        self.posicao_robo = posicao_robo
        self.situacao_esq = situacao_esq
        self.situacao_dir = situacao_dir
        self.situacao_cima = situacao_cima
        self.situacao_baixo = situacao_baixo

    
    def successors(self):
        successors = []
        # Unica ação é mover o robo para a esquerda - Resto igual portanto pega do self

        # IR PARA A ESQUERDA - CONSEQUÊNCIA
        successors.append(RoboAspirador('Ir para a esquerda','1',self.situacao_esq,self.situacao_dir,self.situacao_cima,self.situacao_baixo))

        # IR PARA A DIREITA
        successors.append(RoboAspirador('Ir para a direita','2',self.situacao_esq,self.situacao_dir,self.situacao_cima,self.situacao_baixo))

        # IR PARA A CIMA
        successors.append(RoboAspirador('Ir para a direita','3',self.situacao_esq,self.situacao_dir,self.situacao_cima,self.situacao_baixo))
        
        # IR PARA A BAIXO
        successors.append(RoboAspirador('Ir para a direita','4',self.situacao_esq,self.situacao_dir,self.situacao_cima,self.situacao_baixo))

        # LIMPAR
        # LIMPAR A 1
        if self.posicao_robo == '1':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,'LIMPO',self.situacao_dir,self.situacao_cima,self.situacao_baixo))
        # LIMPAR A DIREITA
        if self.posicao_robo == '2':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,self.situacao_esq,'LIMPO',self.situacao_cima,self.situacao_baixo))

        if self.posicao_robo == '3':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,self.situacao_esq,self.situacao_dir,'LIMPO',self.situacao_baixo))

        if self.posicao_robo == '4':
            successors.append(RoboAspirador('Limpar',self.posicao_robo,self.situacao_esq,self.situacao_dir,self.situacao_cima,'LIMPO'))

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