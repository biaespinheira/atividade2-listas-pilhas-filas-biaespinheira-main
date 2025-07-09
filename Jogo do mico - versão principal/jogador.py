"""Criação da classe 'Jogador', uma lista simplesmente encadeada que armazena as cartas
de cada jogador, e também serve como 'nó' da lista circular 'Ordem'"""

from carta import Carta
from baralho import Baralho

class Jogador: # Lista simplesmente encadeada

    def __init__(self,nome=""):
        """Inicializa o jogador como uma lista simplesmente encadeada"""

        self._inicio     = None
        self.numCartas   = 0
        self.pares       = Baralho () # Pilha -> baralho

        # Guarda o nome do jogador
        self.nome = nome
        # Guarda o próximo jogador
        self.prox = None
        # Inicializa a cor como branco
        self.cor = "\033[0;30;47m"

    def getTamanho(self):
        """ Retorna o número de elementos da lista simplesmente encadeada"""
        return self.numCartas

    def getProx(self):
        """ Retorna o próximo jogador"""
        return self.prox

    def setProx(self,proximo_jogador):
        """ Modifica o próximo jogador.
        
        Parâmetros:
        proximo_jogador -- variável do tipo 'Jogador'."""

        # Verifica o tipo
        if type(proximo_jogador) == Jogador:
            # Define o próximo se o tipo corresponder a "Jogador"
            self.prox=proximo_jogador

        # Se o tipo não corresponder define o próximo como "None"
        else:
            self._prox = None

    def getNome(self):
        """ Retorna o nome do jogador"""
        return self.nome

    def getCor(self):
        """ Retorna a cor do jogador"""
        return self.cor
    
    def setCor(self,novaCor):
        """ Modifica a cor do jogador"""
        self.cor=novaCor

    def getNumCartas(self):
        """ Retorna o número de cartas na mão do jogador"""
        return self.numCartas

    def getPares(self):
        """ Retorna a pilha de pares do jogador"""
        return self.pares   

    def is_empty(self):
        """ Verifica se a lista está vazia"""
        return self.numCartas==0
    
    def recebe(self,n: Carta): # Insert
        """Adiciona uma carta no ínicio da lista.

        Parâmetros:

        n -- variável do tipo 'Carta'"""

        if n==None or type(n)!=Carta:
            return 

        novaCarta = n
        novaCarta.setProx(self._inicio)
        self._inicio = novaCarta
        self.numCartas += 1
        return n

    def perde(self, indice): # Remove a partir da posição
        """Remove uma carta do baralho a partir de seu índice.

        Parâmetros:
        ind -- número do tipo inteiro"""

        # Verifica se o índice existe
        if indice>self.numCartas or indice<=0:
            return None
        
        # Inicializa a carta corrente
        carta=self._inicio

        # Testa o primeiro índice
        if indice==1:
            # Retira a carta se o índice corresponder
            self._inicio=carta.getProx()
            self.numCartas-=1
            return carta
        
        # Acha a carta de índice correspondente
        for i in range (1,indice-1):
            carta=carta.getProx()
        
        # Retira a carta de índice correspondente
        proxCarta = carta.getProx()
        carta.setProx(proxCarta.getProx())
        self.numCartas-=1

        # Retorna a carta removida
        return proxCarta

    def __abaixa(self,n):
            """ Percorre uma lista a partir de uma carta 'n' para achar 
            e remover a primeira carta de mesmo dado que 'n'.

            Parâmetros:
            n -- variável do tipo 'Carta'"""

            # Se não existe próxima carta
            if n == None:
                return None
            
            # Atualiza a carta corrente e a próxima carta
            carta=n
            proxCarta=carta.getProx()

            # Verifica as próximas cartas até achar uma com mesmo número ou letra
            while proxCarta != None and proxCarta.getDado() != n.getDado():
                # Atualiza a carta corrente 
                carta = proxCarta
                proxCarta = carta.getProx()

            # Se a lista chegou ao fim e não encontrou n
            if proxCarta == None:
                return None
                
            # Se achou carta igual ela é removida
            carta.setProx(proxCarta.getProx())
            self.numCartas -= 1

            # Retorna a carta removida
            return proxCarta

    def abaixa_pares(self):
        '''Essa função acha os pares olhando uma carta e procurando a primeira 
        carta de dado igual que vier em seguida através do método '__abaixa'. 
        Se o par for encontrado ambas as cartas são abaixadas e retiradas da mão do 
        jogador. '''

        # Armazena a quantidade inicial de cartas do jogador
        n_inicial=self.numCartas

        # Inicializa a carta a ser verificada
        carta=self._inicio

        # Armazena a posição da carta 
        i=1

        while carta!=None and carta.getProx()!=None:

            # Procura o par da carta e o remove da lista se encontrar
            par=self.__abaixa(carta)

            # Se achar o par:
            if par!=None:
                # Coloca o par e a carta na pilha "pares"
                self.pares.push(par)
                self.pares.push(carta)

                # Remove a carta
                self.perde(i)
                i-=1

            # Atualiza a carta corrente e a sua posição
            carta=carta.getProx()
            i+=1

        # Armazena a quantidade final de cartas na mão do jogador
        n_final=self.numCartas

        # Verifica se algum par foi abaixado
        if n_final==n_inicial:
            return False
        else:
            return True

    def abaixa_par(self):

        # Inicializa a carta corrente com a última carta recebida
        carta=self._inicio

        # Procura o par da carta e o remove da lista se encontrar
        par=self.__abaixa(carta)

        # Se achar o par:
        if par!=None:
            # Coloca o par e a carta na pilha "pares"
            self.pares.push(par)
            self.pares.push(carta)

            # Remove a carta recebida (primeira posição)
            self.perde(1)

            # Se achar o par retorna True
            return True
        
        # Se não achar retorna False
        return False

    def ver_mao(self):
            """ Formata a saída do baralho para que o jogador veja suas cartas"""

            # Guarda o número de cartas
            n=self.numCartas
            # Inicializa a string da saída
            outstr=""
            # Inicializa o 'k' como 0 para o caso de ter até 13 cartas
            k=0
            # Inicializa a carta corrente
            carta=self._inicio
            # Inicializa a cor
            cor=""
            # Define o fundo como branco
            fundo="\033[0;30;47m"

            # Verifica se existem mais de 13 cartas
            if n>13:
                # Se existirem a saída é formatada para caber no terminal
                k=13
                # Quebra de linha
                outstr="\n"
            
                # Guarda na string 'outstr' o topo das primeiras 13 cartas
                for i in range (k):
                    # Guarda o naipe da carta corrente
                    naipe=carta.getNaipe()

                    if (naipe=="♣"):         #paus -> azul
                        cor="\033[0;34;47m" 
                    elif (naipe=="♠"):       #espadas -> azul
                        cor="\033[0;34;47m" 
                    elif (naipe=="♥"):       #copas -> vermelho
                        cor="\033[0;31;47m"      
                    else: #naipe=="♦"        #ouros -> vermelho
                        cor="\033[0;31;47m"
                    
                    outstr+=fundo+cor+naipe+"    \033[m "
                    # Atualiza a carta corrente
                    carta=carta.getProx()

                # Quebra de linha
                outstr+="\n"

                # Volta para a carta inicial
                carta=self._inicio

                # Guarda na string 'outstr' o meio das primeiras 13 cartas
                for i in range (k):
                    # Guarda o dado da carta corrente
                    dado=carta.getDado()
                    if dado=="10":
                        outstr+=fundo+" "+dado+"  \033[m "
                    else:
                        outstr+=fundo+"  "+dado+"  \033[m "
                    # Atualiza a carta corrente
                    carta=carta.getProx()

                # Quebra de linha
                outstr+="\n"

                # Volta para a carta inicial
                carta=self._inicio

                # Guarda na string 'outstr' a base das primeiras 13 cartas
                for i in range (k):
                    # Guarda o naipe da carta corrente
                    naipe=carta.getNaipe()

                    if (naipe=="♣"):         #paus -> azul
                        cor="\033[0;34;47m" 
                    elif (naipe=="♠"):       #espadas -> azul
                        cor="\033[0;34;47m" 
                    elif (naipe=="♥"):       #copas -> vermelho
                        cor="\033[0;31;47m"      
                    else: #naipe=="♦"        #ouros -> vermelho
                        cor="\033[0;31;47m" 

                    outstr+=fundo+"    "+cor+naipe+"\033[m "

                    # Atualiza a carta corrente
                    carta=carta.getProx()

            # Duas quebras de linha
            outstr+="\n\n"
        
            # Guarda a carta corrente (1° ou 13°)
            carta_atual=carta

            # Guarda na string 'outstr' o topo das cartas que faltam
            for i in range (k,n):

                # Guarda o naipe da carta corrente
                naipe=carta.getNaipe()

                if (naipe=="♣"):         #paus -> azul
                    cor="\033[0;34;47m" 
                elif (naipe=="♠"):       #espadas -> azul
                    cor="\033[0;34;47m" 
                elif (naipe=="♥"):       #copas -> vermelho
                    cor="\033[0;31;47m"      
                else: #naipe=="♦"        #ouros -> vermelho
                    cor="\033[0;31;47m"
                    
                outstr+=fundo+cor+naipe+"    \033[m "
                
                # Atualiza a carta corrente
                carta=carta.getProx()

            # Quebra de linha
            outstr+="\n"

            # Volta a carta corrente
            carta=carta_atual

            # Guarda na string 'outstr' o meio das cartas que faltam
            for i in range (k,n):
                
                # Guarda o dado da carta corrente
                dado=carta.getDado()

                if dado=="10":
                    outstr+=fundo+" "+dado+"  \033[m "
                else:
                    outstr+=fundo+"  "+dado+"  \033[m "

                # Atualiza a carta corrente
                carta=carta.getProx()

            # Quebra de linha
            outstr+="\n"
            
            # Volta a carta corrente
            carta=carta_atual

            # Guarda na string 'outstr' a base das cartas que faltam
            for i in range (k,n):

                # Guarda o naipe da carta corrente
                naipe=carta.getNaipe()

                if (naipe=="♣"):         #paus -> azul
                    cor="\033[0;34;47m" 
                elif (naipe=="♠"):       #espadas -> azul
                    cor="\033[0;34;47m" 
                elif (naipe=="♥"):       #copas -> vermelho
                    cor="\033[0;31;47m"      
                else: #naipe=="♦"        #ouros -> vermelho
                    cor="\033[0;31;47m" 

                outstr+=fundo+"    "+cor+naipe+"\033[m "

                # Atualiza a carta corrente
                carta=carta.getProx()
            
            # Quebra de linha
            outstr+="\n"

            # Retorna a string formatada
            return outstr

    def select(self,ind=0):
        """Formata a saída do baralho virado para baixo.
        Também pode receber um índice para que mostre a carta selecionada.

        Parâmetros:
        ind -- número do tipo inteiro"""

        # Inicializa o 'k' como 0 para o caso de ter até 13 cartas
        k=0

        # O ind é modificado para selecionar o índice corrspondente
        ind-=1

        # Obtem o número de cartas
        n=self.getTamanho()

        # Quebra de linha
        outstr="\n"

        # Verifica se existem mais de 13 cartas na mão do jogador
        if n>13:
            # Se existirem a saída é formatada para caber no terminal
            k=13

            # Adiciona na string 'outstr' o topo as primeiras 13 cartas
            for i in range (k):
                # Mostra a carta colorida se o índice for selecionado
                if i==ind:
                    outstr+="\033[36m╔══╗ \033[m"
                else:
                    outstr+="\033[1;37m╔══╗ \033[m"

            # Quebra de linha
            outstr+="\n"

            # Adiociona na string 'outstr' o meio das primeiras 13 cartas
            for i in range (k):
                # Mostra a carta colorida se o índice for selecionado
                if i==ind:
                    outstr+="\033[34m║❖ ║ \033[m"
                else:
                    outstr+="║❖ ║ "

            # Quebra de linha
            outstr+="\n"

            # Adiciona na string 'outstr' a base das primeiras 13 cartas
            for i in range (k):
                # Mostra a carta colorida se o índice for selecionado
                if i==ind:
                    outstr+="\033[34m╚══╝ \033[m"
                else:
                    outstr+="╚══╝ "

        # Quebra de linha
        outstr+="\n"

        # Adiciona na string 'outstr' o topo das cartas que restaram 
        for i in range (k,n):
            # Mostra a carta colorida se o índice for selecionado
            if i==ind:
                outstr+="\033[36m╔══╗ \033[m"
            else:
                outstr+="\033[1;37m╔══╗ \033[m"

        # Quebra de linha
        outstr+="\n"

        # Adiciona na string 'outstr' o meio das cartas que restaram
        for i in range (k,n):
            # Mostra a carta colorida se o índice for selecionado
            if i==ind:
                outstr+="\033[34m║❖ ║ \033[m"
            else:
                outstr+="║❖ ║ "

        outstr+="\n"

        # Adiciona na string 'outstr' a base das cartas que restaram
        for i in range (k,n):
            # Mostra a carta colorida se o índice for selecionado
            if i==ind:
                outstr+="\033[34m╚══╝ \033[m"
            else:
                outstr+="╚══╝ "

        # Quebra de linha
        outstr+="\n"

        # Retorna a string formatada 
        return outstr

    def cartas(self):
        
        if self.is_empty():
            return "[]"
        
        carta=self._inicio
        outstr=""

        for i in range (self.numCartas):
            outstr+=carta._dado+carta._naipe+" "
            carta=carta._prox

        return outstr

if __name__=="__main__":   
    baralho = Baralho ()
    baralho.gerar_baralho()
    print (baralho)
    baralho.gerar_ace()
    print (baralho)
    mico = baralho.pop_mico()

    #comentar depois
    print(mico)
    
    jogador1= Jogador ("Bia")

    jogador_atual= jogador1
    while baralho.getTamanho()!=26:
        carta=baralho.pop()
        #print(carta)
        jogador_atual.recebe(carta)

    print("antes:",jogador_atual.cartas())
    print(jogador_atual.ver_mao())
    jogador_atual.abaixa_par()
    print("depois",jogador_atual.cartas())

    print(jogador_atual.ver_mao())

    print(jogador_atual.select(3))
    print(jogador_atual.ver_mao())
    jogador_atual.abaixa_pares()
    print(jogador_atual.ver_mao())