"""Criação da classe Baralho (), que atua como uma pilha para o baralho 
completo do jogo e também para pilha de pares de cada jogador."""

import random
from datetime import datetime
from carta import Carta

class Pilha:

    def __init__(self):
        ''' Inicializa a pilha com no máx 52 elementos'''
        self.vPilha     = [0]*52 
        self._maxElem    = 52 
        self._topo       = 0

        return 

    def push(self, carta): 
        """ Adiciona um elemento no final da pilha"""

        # Verifica se a pilha está cheia
        if self.full():
            return

        # A pilha é atualizada com a novo elemento
        self[self._topo] = carta
        self._topo += 1

        return

    def pop(self):
        """ Remove o último elemento do final da pilha """

        # Verifica se a pilha está vazia
        if self.empty():
            return None

        # Atualiza o topo
        self._topo -= 1

        # Retorna o elemento removido
        if self._topo>=0:
            return self[self._topo]
           
    def empty(self):
        """ Verifica se a pilha está vazia"""
        if self._topo==0:
            return True
        return False

    def full(self):
        """ Verifica se a pilha está cheia"""

        return self._topo == self._maxElem

    def size(self):
        """Retorna o tamanho da pilha"""
        return self._topo

    def __getitem__(self, indice: int):
        """Retorna o elemento de índice correspondente

        Parâmetros:
        indice -- número do tipo inteiro"""

        # Verifica se o índice existe 
        if indice>=0:
            return self.vPilha[indice]
        else:
            return None
    
    def __setitem__(self,indice: int, k):
        """Modifica o elemento de índice correspondente
        
        Parâmetros:
        indice -- número do tipo inteiro
        k      -- novo elemento"""

        # Verifica se o índice existe 
        if indice>=0 and indice<self._maxElem:
            self.vPilha[indice]=k
    
    def getTamanho (self):
        """ Retorna a quantidade de cartas no baralho"""
        return self._topo

class Baralho (Pilha):

    def __init__(self):
        """Inicializa o baralho como uma pilha de no máx 52 elementos"""

        super().__init__()
        return 
        
    def gerar_baralho(self):
        ''' Método adicional que cria o baralho completo ordenado'''

        # Cria 4 objetos de naipes diferentes para cada número de 1 à 13
        for i in range (1,14):

            # Armazenando os dados das cartas
            dado=i

            # Inicializa alguns dados como strings de números (2-10)
            if dado>1 and dado<=10 :
                dado=str(dado)

            # Alguns dado são inicializados com sua letra correspondente
            else:
                if (dado==11):
                    dado = "J"
                elif (dado==12):
                    dado = "Q"
                elif (dado==13):
                    dado = "K"
                elif (dado==1):
                    dado = "A"

            # Para cada dado, quatro cartas são inicializadas com naipes diferentes
            carta = Carta (dado,"♣") #paus
            self.push(carta) # Carta é adicionada no objeto do tipo baralho
            carta = Carta (dado,"♠") #espadas
            self.push(carta)
            carta = Carta (dado,"♥") #copas
            self.push(carta)
            carta = Carta (dado,"♦") #ouros
            self.push(carta)
        
        return 
    
    def gerar_ace(self):
        """ Embaralha as cartas do baralho (Troca aleatóriamente os objetos 
        do tipo 'Carta' de posição)"""

        # Obtem o tamanho da pilha baralho
        n=self.size()

        # Garante a geração aleatória de índices
        random.seed(datetime.now().timestamp())

        # Embaralha os indices do baralho, criando uma lista de índices aleatórios
        ind = random.sample(range(0,n), n) 

        # Cria uma nova pilha de baralho para armazenar o 'ace'
        ace = Baralho()

        # Adiciona aleatóriamente as cartas da pilha antiga na nova pilha
        for i in range (n):
            ace.push(self[ind[i]]) # As cartas são adicionadas na ordem aleátoria da lista 'ind'

        # Sobrescreve a pilha antiga com a nova embaralhada
        self.vPilha=ace.vPilha
        
        return 
    
    def pop_mico(self): 
        """ Remove um elemento aleatório do baralho """

        # Se a pilha está vazia, nada é removido
        if self.empty():
            return
        
        # Armazena o tamanho da pilha
        n=self.size()

        # Garante a geração aleatória do índice
        random.seed(datetime.now().timestamp())

        # Gera um índice aleatório para ser removido
        k= random.randint(0,n-1)

        # Armazena o elemento com o índice correspondente
        elem= self[k]

        # Atualiza o topo
        self._topo-=1

        # Realoca os outros elementos do baralho
        for i in range (k,n-1):
            self[i]=self[i+1]
        
        return elem

    def mostrar_topo(self):
        """ Formatação para imprimir o último elemento adicionado na pilha"""

        # Verifica se a pilha está vazia
        if self.empty():
            return ""
        
        # Encontra o último elemento adicionado
        carta=self[self._topo-1]
        # Armazena seu dado
        dado= carta.getDado()
        # Armazena seu naipe
        naipe= carta.getNaipe()

        # Variável par armazenar cor do naipe
        cor=""
        # Define o fundo da carta como branco
        fundo="\033[0;30;47m"

        if (naipe=="♣"):         #paus -> azul
            cor="\033[0;34;47m" 
        elif (naipe=="♠"):       #espadas -> azul
            cor="\033[0;34;47m" 
        elif (naipe=="♥"):       #copas -> vermelho
            cor="\033[0;31;47m"      
        else: #naipe=="♦"        #ouros -> vermelho
            cor="\033[0;31;47m"   

        # Formatação de saída da última carta
        outstr="\n"+fundo+cor+naipe+"    \033[m══╗"
        if dado=="10":
            outstr+="\n"+fundo+" "+dado+"  \033[m  ║"
        else:
            outstr+="\n"+fundo+"  "+dado+"  \033[m  ║"
        outstr+="\n"+fundo+"    "+cor+naipe+"\033[m  ║"
        outstr+="\n  ╚════╝"

        # Retorna a string com a formatação da saída
        return outstr
    
    def __str__(self):
    
        if self.empty()==True:
            return "[]"

        # Guarda o índice do último elemento da pilha
        n=self.size()

        outstr=""

        # Armazena as cartas
        for i in range (n):
            dado=self[i].getDado()
            naipe=self[i].getNaipe()
            outstr+=dado+" "+naipe+" |"

        return outstr

# Teste
if __name__ == '__main__':

    baralho = Baralho()
    baralho.gerar_baralho()
    print(baralho)
    baralho.gerar_ace()
    print(baralho)
    while baralho.empty()!=True:
        print(baralho.pop())
        print(baralho)