""" Criação da classe 'Ordem', uma lista circular para objetos do tipo 'Jogador'"""
from jogador import Jogador
import random
from datetime import datetime

class Ordem: #Lista Circular

    def __init__(self):
        """ Inicializa a ordem com 0 jogadores"""
        self.inicio = None
        self.numPlayers = 0
    
    def getInicio(self):
        """ Retorna o jogador(nó) ínicial da lista"""
        return self.inicio
    
    def getNumPlayers(self):
        """ Retorna o número de jogadores(nós) da lista"""
        return self.numPlayers
    
    def is_empty(self):
        """ Verifica se a lista ordem está vazia"""
        return self.inicio == None

    def game_over(self):
        """ Retorna se o jogo acabou (Existe apenas um nó)"""
        # Se existir apenas um jogador
        if self.inicio!=None and self.inicio==self.inicio.prox:
            return True
        return False

    def __str__(self):
        """ Formata a saída com os 'nomes' dos jogadores"""

        # Se o jogo acabar
        if self.game_over():
            outstr="Sem jogadores"
            return outstr
        
        outstr=""
        # Inicializa o jogador corrente
        jogadorCor = self.inicio

        while True:
            # Adiciona na saída os nomes de cada jogador
            outstr+=str(jogadorCor.getNome())+" "
            jogadorCor = jogadorCor.getProx()

            # Se percorreu a lista toda
            if jogadorCor == self.inicio:
                break
        
        return outstr

    def new_player(self, novo_jogador: Jogador): # Insert
        """ Adiciona um novo jogador (nó) na lista"""

        # Verifica se a lista está vazia
        if self.is_empty():
            # O inicio e o fim são atualizados com o novo_jogador
            self.inicio = novo_jogador
            self.fim = novo_jogador

            # O próximo jogador é modificado 
            novo_jogador.setProx(novo_jogador)

            # Aumenta o número de jogadores (nós)
            self.numPlayers+=1

            return 
        
        # O novo jogador é inserido na ordem entre o fim e o início
        novo_jogador.setProx(self.inicio)
        self.fim.setProx(novo_jogador)
        self.fim = novo_jogador
        self.numPlayers+=1

    def player_left(self, k:Jogador): # Remove
        """ Retira um jogador (nó) da lista circular.
        
        Parâmetros:
        k -- variável do tipo 'Jogador' a ser removida"""

        # Inicializa o jogador corrente
        jogador = self.inicio

        # Armazena o anterior
        prev = None

        while True:
            if jogador == k:

                # Se o jogador a ser removido é o primeiro
                if jogador == self.inicio:  
                    # Inicializa o fim como o início
                    fim = self.inicio

                    # Procura o fim da lista
                    while fim.getProx() != self.inicio:
                        fim = fim.getProx()

                    # Inicio é atualizado para o elemento depois
                    self.inicio = jogador.getProx()

                    # O fim é atualizado para o novo início
                    fim.setProx(self.inicio)
                
                # Se o jogador não for o primeiro
                else:

                    # 'Retira' o jogador da lista
                    prev.setProx(jogador.getProx())

                # Número de jogadores é atualizado
                self.numPlayers-=1

                # Retorna o jogador removido
                return k
            
            # Atualiza o jogador anterior
            prev = jogador

            # Atualiza o jogador corrente
            jogador = jogador.getProx()

            # Se a lista for percorrida e não achar
            if jogador == self.inicio:
                return None

# Testes
if __name__=="__main__":
    jogador1= Jogador("B")
    jogador2= Jogador("I")
    jogador3= Jogador("N")
    jogador4= Jogador("L")
    ordem = Ordem()
    ordem.new_player(jogador1)
    ordem.new_player(jogador2)
    ordem.new_player(jogador3)
    ordem.new_player(jogador4)

    print(ordem)
    print(ordem.getNumPlayers())
    ordem.player_left(jogador2)
    print(ordem.numPlayers)

    print(ordem)
    print(ordem.numPlayers)
    print(ordem)
