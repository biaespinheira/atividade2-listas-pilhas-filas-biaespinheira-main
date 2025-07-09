"""Criação da classe carta, essa classe instancia objetos que atuam como um 'nó'
da lista simplesmente encadeada 'Jogador ()' ou como elemento da pilha 'Baralho'."""

class Carta: # Nó

    def __init__ (self, carta: str, naipe: str):

        self._dado = carta
        self._naipe = naipe
        self._prox = None

    def setProx (self, prox):
        """Define o próximo elemento do objeto
        
        Parâmetros:
        prox -- objeto do tipo 'Carta'
        """

        # Verifica o tipo
        if type(prox) == Carta:
            # Define o próximo se o tipo corresponder a "Carta"
            self._prox = prox

        # Se o tipo não corresponder define o próximo como "None"
        else:
            self._prox = None

    def getProx (self):
        """Retorna o próximo elemento"""

        return self._prox
    
    def getDado (self):
        """Retorna o 'dado' do objeto, no caso,
        o número ou letra da carta em forma de
        string"""

        return self._dado
    
    def getNaipe(self):
        """Retorna o 'naipe' do objeto, no caso,
        o naipe da carta em forma de string"""

        return self._naipe
    
    def __str__ (self):
        """Imprime o objeto do tipo carta"""

        # Obtem o dado e o naipe do objeto
        dado= self._dado
        naipe= self._naipe

        # Variável para armazenar a cor do naipe
        cor=""
        # Define a cor de fundo como branco
        fundo="\033[0;30;47m"

        # Define a cor do naipe
        if (naipe=="♣"):         #paus -> azul
            cor="\033[0;34;47m" 
        elif (naipe=="♠"):       #espadas -> azul
            cor="\033[0;34;47m" 
        elif (naipe=="♥"):       #copas -> vermelho
            cor="\033[0;31;47m"      
        else: #naipe=="♦"        #ouros -> vermelho
            cor="\033[0;31;47m"      

        # Formatação da carta
        outstr="\n"+fundo+cor+naipe+"    \033[m"

        if dado=="10":
            outstr+="\n"+fundo+" "+dado+"  \033[m"
        else:
            outstr+="\n"+fundo+"  "+dado+"  \033[m"
        outstr+="\n"+fundo+"    "+cor+naipe+"\033[m"
        outstr+="\n"

        # Retorna uma string com a formatação da carta
        return outstr

# Teste 
if __name__=="__main__":
    aspaus= Carta ("J","♦")
    print(aspaus)
    dezouros= Carta ("10","♦")
    aspaus.setProx(dezouros)
    print(aspaus.getProx())