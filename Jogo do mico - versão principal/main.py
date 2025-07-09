""" Jogo
Obs: COLOQUE O TERMINAL EM TELA CHEIA"""

from baralho import Baralho
from jogador import Jogador
from ordem import Ordem
from funcoes import *

print(tela_inicio()) # Tela inicial
input() # -> Enter para iniciar
print(barra_cartas()) # Barra de cartas
# Cor 
fcor="\033[m"

# Recebe a quantidade de jogadores
num_jogadores=input("\n\033[0;30;47m Quantidade de jogadores: (2-4)\033[m\n\n")

# Se a quantidade for inválida sinaliza e repete o comando
while is_int(num_jogadores)==False or int(num_jogadores)<2 or int(num_jogadores)>4:
    print("\n\033[0;30;41m Quantidade inválida!\033[m\n")
    print("\n\033[0;30;47m Digite uma quantidade válida: (mínimo: 2 | máximo: 4) \033[m\n")
    num_jogadores=input()
num_jogadores=int(num_jogadores)

# Cria o jogo 
jogo = Ordem ()

# Adiciona os jogadores no jogo 
for i in range (num_jogadores):

    nome_jogador=input(f"\n\033[0;30;47m Nome do {i+1}° jogador: \033[m\n\n")

    # Cria o objeto jogador com o nome inserido
    jogador = Jogador(nome_jogador.upper())

    print("\n\033[0;30;47m Digite para escolher uma cor: \033[m\n")
    cor=input('\033[0;30;46m "1" - AZUL \033[m   \033[0;30;45m "2" - ROXO \033[m   \033[0;30;42m "3" - VERDE \033[m   \033[0;30;43m "4" - AMARELO \033[m   \033[0;30;47m"" - CINZA \033[m\n\n')
    if cor=="1": 
        cor="\033[0;30;46m"
    elif cor=="2":
        cor="\033[0;30;45m"
    elif cor=="3":
        cor="\033[0;30;42m"
    elif cor=="4":
        cor="\033[0;30;43m"
    else:
        cor="\033[0;30;47m"
    
    # Modifica a cor do jogador
    jogador.setCor(cor)

    # Adiciona o jogador na lista circular 'Jogo'
    jogo.new_player(jogador)

    print(f"\n{cor} Jogador adicionado!!! \033[m\n")

# Mostra os jogadores atuais
print("\n\033[0;30;47m Jogadores atuais: \033[m", jogo,"\n")

# Inicializa, embaralha e tira o mico do baralho
baralho = Baralho ()
baralho.gerar_baralho()
print(" Embaralhando ...\n")
baralho.gerar_ace()
print(" Removendo o mico ...\n")
mico = baralho.pop_mico()

# Inicializa o jogador atual
jogador_atual=jogo.getInicio()

print(" Distribuindo cartas ...\n")

# Enquanto houver cartas, distribui para os jogadores
while baralho.empty()!=True:
    # Remove a carta do baralho
    carta=baralho.pop()
    # Entrega ao jogador
    jogador_atual.recebe(carta) #Insert 
    # Passa para o próximo jogador
    jogador_atual=jogador_atual.prox

# Volta para o primeiro jogador
jogador_atual=jogo.getInicio()

# Mostra a distribuição das cartas
for i in range(jogo.getNumPlayers()):
    nome= jogador_atual.getNome()
    cor= jogador_atual.getCor()
    print(f"{cor} {nome}: {fcor}", jogador_atual.select())
    jogador_atual=jogador_atual.getProx()

# Inicializa o próximo jogador
proximo_jogador=jogador_atual.getProx()

# Formatação
print(barra_cartas())
print(play())
print(barra_cartas())
input()

# Conta as rodadas
rodada=1

# Inicia o jogo
while True:

    # Armazena a cor do jogador atual
    cor=jogador_atual.getCor()

    # Vez do jogador
    print(f"{cor} Vez de: {jogador_atual.getNome()} {fcor}")

    if rodada<=jogo.getNumPlayers(): # Se for a primeira rodada

        # Menu: 1- procurar pares | 2- ver cartas
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar pares {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")

        # Verifica se opção é válida
        while option!="1" and option!="2":
            print("\n\033[0;30;41m Opção inválida!\033[m\n")    
            option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar pares {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")
        
        # Mostra as cartas e cria um novo menu
        if option=="2":
            print(jogador_atual.ver_mao())
            option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar pares {fcor}\n\n")
            while option!="1":
                print("\n\033[0;30;41m Opção inválida!\033[m\n") 
                option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar pares {fcor}\n\n")

        # Se opção foi "1",  procura e "abaixa" todos os pares na mão do jogador
        print(f"\n{cor} Procurando pares... {fcor}\n")
        abaixa=jogador_atual.abaixa_pares() 

        print(f"\n{cor} Pares Formados!!! {fcor}\n")

        # Armazena os pares do jogador
        pares=jogador_atual.getPares()

        # Mostra o último par
        print(f"\n{cor} Último par formado: {fcor}\n",pares.mostrar_topo())

    # Menu: 1- Pegar carta | 2- Ver cartas
    option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para pegar carta de {proximo_jogador.getNome()} {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")

    # Verifica se opção é válida
    while option!="1" and option!="2":
        print("\n\033[0;30;41m Opção inválida!\033[m\n")    
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para pegar carta de {proximo_jogador.getNome()} {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")
    
    # Mostra as cartas e cria um novo menu
    if option=="2":
        print(jogador_atual.ver_mao())
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para pegar carta de {proximo_jogador.getNome()} {fcor}\n\n")
        while option!="1":
            print("\n\033[0;30;41m Opção inválida!\033[m\n") 
            option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para pegar carta de {proximo_jogador.getNome()} {fcor}\n\n")
        
    # Se a opção foi 1
    print(f"\n{cor} Retire uma carta de {proximo_jogador.getNome()} {fcor}\n")
    print(proximo_jogador.select())

    # Pede posição da carta que deseja retirar
    ind=input(f"\n{cor} Digite a carta que deseja retirar: {fcor}\n\n")

    # Verifica se posição é válida
    while is_int(ind)==False or int(ind)>proximo_jogador.getNumCartas() or int(ind)<1:
        print("\n\033[0;30;41m Opção inválida!\033[m\n")
        ind=input(f"\n{cor} Digite a carta que deseja retirar: {fcor}\n\n")

    ind=int(ind)
    # Mostra a carta selecionada
    print(proximo_jogador.select(ind))

    # Confimação
    option=input(f"\n{cor} Deseja retirar essa carta? (s/n) {fcor}\n\n")

    # Verifica se a opção é válida, se não for repete o processo
    while option!="s":
        if option!="n":
            print("\n\033[0;30;41m Opção inválida!\033[m\n")
        ind=input(f"\n{cor} Digite a carta que deseja retirar: {fcor}\n\n")
        while is_int(ind)==False or int(ind)>proximo_jogador.getNumCartas() or int(ind)<1:
            print("\n\033[0;30;41m Opção inválida!\033[m\n")
            ind=input(f"\n{cor} Digite a carta que deseja retirar: {fcor}\n\n") 
        ind=int(ind)
        print(proximo_jogador.select(ind))

        option=input(f"\n{cor} Deseja retirar essa carta? (s/n) {fcor}\n\n")
    
    # Retira a carta do próximo jogador e armazena em 'carta'
    carta=proximo_jogador.perde(ind)

    # Mostra a carta
    print(f"\n{cor} A carta escolhida foi: {fcor}\n")
    print(carta)

    # Insere a carta na mão do jogador atual
    jogador_atual.recebe(carta)

    # Menu: 1- procurar um par | 2- ver cartas
    option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar um par {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")

    # Verifica se opção é válida
    while option!="1" and option!="2":
        print("\n\033[0;30;41m Opção inválida!\033[m\n")    
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar um par {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")

    # Mostra as cartas e cria um novo menu    
    if option=="2":
        print(jogador_atual.ver_mao())
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar um par {fcor}\n\n")
        while option!="1":
            print("\n\033[0;30;41m Opção inválida!\033[m\n") 
            option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para procurar um par {fcor}\n\n")

    # Se a opção for 1 procura um par
    print(f"\n{cor} Procurando par ... {fcor}\n")
    abaixa=jogador_atual.abaixa_par()

    # Mostra se encontrou
    if abaixa==True:
        print(f"\n{cor} Par Formado!!! {fcor}\n")
    else:
        print(f"\n{cor} Par não encontrado :( {fcor}\n")

    # Verifica se as cartas do próximo jogador acabaram
    if proximo_jogador.getNumCartas() == 0:
        nova_cor=proximo_jogador.getCor()
        print(f"\n{nova_cor} {proximo_jogador.getNome()} não tem mais cartas e saiu do jogo {fcor}\n")

        # Retira o jogador da lista circular 'jogo'
        jogo.player_left(proximo_jogador)

        # Atualiza o próximo jogador
        proximo_jogador=jogador_atual.getProx()

        # Se só existe um jogador
        if jogo.game_over():
            print(barra_cartas())
            print(fim_de_jogo())
            print(barra_cartas())

            input()

            jogador_restante=jogo.getInicio()
            cor=jogador_restante.getCor()
            print(f"{cor} {jogador_restante.getNome()} perdeu! {fcor}\n")

            # Mostra a carta restante
            print(f"\n{cor} Carta restante: {fcor}")
            print(jogador_restante.ver_mao())

            # Mostra o mico
            print(f"{cor} O mico era: {fcor}")
            print(mico)

            # Finaliza o jogo
            break

        else:
            # Mostra os jogadores restantes
            print(f"\033[0;30;47m Jogadores restantes: \033[m", jogo)

    # Verifica se as cartas do jogador atual acabaram
    if jogador_atual.getNumCartas()==0:

        nova_cor=proximo_jogador.getCor()
        print(f"\n{nova_cor} {jogador_atual.getNome()} não tem mais cartas e saiu do jogo {fcor}\n")

        # Remove o jogador atual da lista circular 'jogo'
        jogo.player_left(jogador_atual)

        # Atualiza o jogador atual e o próximo jogador
        jogador_atual=proximo_jogador
        proximo_jogador=jogador_atual.getProx()

        # Se restou apenas um jogador
        if jogo.game_over():
            print(barra_cartas())
            print(fim_de_jogo())
            print(barra_cartas())

            input()

            jogador_restante=jogo.getInicio()
            cor=jogador_restante.getCor()
            print(f"{cor} {jogador_restante.getNome()} perdeu! {fcor}\n")

            # Mostra a carta restante
            print(f"\n{cor} Carta restante: {fcor}")
            print(jogador_restante.ver_mao())

            # Mostra o mico
            print(f"\n{cor} O mico era: {fcor}\n")
            print(mico)

            # Finaliza o jogo
            break
        
        else:
            # Mostra os jogadores restantes
            print(f"\033[0;30;47m Jogadores restantes: \033[m", jogo)
    
    # Armazena os pares do jogador
    pares=jogador_atual.getPares()

    # Mostra o último par
    print(f"\n{cor} Último par formado: {fcor}\n",pares.mostrar_topo())

    # Menu: 1- Finalizar vez | 2- Ver cartas
    option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para finalizar sua vez {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")
    
    # Verifica se opção é válida
    while option!="1" and option!="2":
        print("\n\033[0;30;41m Opção inválida!\033[m\n")    
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para finalizar sua vez {fcor}  {cor}'2' - para ver suas cartas {fcor}\n\n")
    
    # Mostra as cartas e cria um novo menu
    if option=="2":
        print(jogador_atual.ver_mao())
        option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para finalizar sua vez {fcor}\n\n")
        while option!="1":
            print("\n\033[0;30;41m Opção inválida!\033[m\n") 
            option=input(f"\n{cor} Digite: {fcor}\n\n{cor} '1' - para finalizar sua vez {fcor}\n\n")

    # Atualiza o jogador atual e o próximo jogador
    jogador_atual=proximo_jogador
    proximo_jogador=jogador_atual.getProx()

    # Atualiza a rodada
    rodada+=1

    # Formatação
    print("\n"*5)
    print(barra_cartas2()*3)
    print(prox_player(jogador_atual.getCor()),"\n")
    print(barra_cartas2()*3)
    input()

    # Repete para o próximo jogador