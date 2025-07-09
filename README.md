[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fqfjTGDI)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11218671&assignment_repo_type=AssignmentRepo)
# Atividade 2 - Simulando um Jogo de Baralho

## Objetivos da Atividade:

O objetivo principal da atividade é aplicar os conceitos de **Tipos Abstratos de Dados (TAD) Lineares**, ou seja, **Listas Encadeadas**, **Pilhas** e **Filas** [1] apresentados em sala de aula, no contexto de um problema real e prático.

Os alunos deverão analisar o problema proposto, e definir qual o melhor TAD a ser utilizado na resolução do problema. Mais de um TAD pode ser necessário para que se possa atingir a solução do problema. 

Escolhidos os TADs, sua implementação deverá ser integrada ao problema e uma solução computacional codificada em linguagem Python. Lembrando que os recursos da linguagem Python podem ser utilizados, desde que não entrem em conflito com o gerenciamento dos seus TADs. 

## Motivação:

Jogos eletrônicos costumam demandar por estruturas de dados eficientes e robustas em várias de suas etapas. Mesmo jogos simples podem requerer estruturas de dados apropriadas para que o roteiro do jogo possa ser implementado de forma eficiente. 

Jogos tradicionais ainda são bastante comuns como passatempos. Nessa categoria, os jogos baseados em baralhos de cartas apresentam uma vasta gama de opções [2]. Um dos mais simples e divertido é o Mico [3]. Nesse jogo o objetivo é formar pares de cartas, a partir das cartas na mão do jogador. No inicio do jogo, uma carta é retirada do baralho (o mico). Dessa forma, um par deixará de ser formado. O "perdedor" é aquele jogador que ficar com a carta "par" do "mico". 

O jogo é jogado com 1 baralho de cartas completo. Após ser embaralhado, uma carta é retirada e as demais distribuidas entre os jogadores. Na primeira etapa os jogadores avaliam suas mãos e retiram os pares de cartas iguais, separando-as em um monte a sua frente. Com o restante das cartas que não possuem par, cada jogador na sua vez retira uma carta aleatóriamente da mão de outro jogador (mantendo uma regra de ciclagem, horária ou anti-horária). Caso a nova carta faça um par com alguma carta de sua mão, o jogador coloca o par no monte de cartas a sua frente. Esse passo é realizado até que reste apenas uma carta na mão de um jogador: o mico. Esse jogador é o perdedor.  

## O Problema:

Uma empresa de desenvolvimento de jogos quer contratar um novo membro para a sua equipe de desenvolvimento de jogos infantis educativos. Sabendo que os alunos da disciplina de Estrutura de Dados na UFBA são muito bons, decidiu fazer a primeira etapa de sua seleção durante a disciplina propondo um desafio simples mas instigante: desenvolver um simulador de jogo de Mico para crianças, para ser jogado em sua plataforma on-line de jogos educativos. 

Como o desafio é parte do processo seletivo, o interesse é avaliar o conhecimento dos concorrentes para projetar e desenvolver o núcleo jogo, ou seja, os **TADs** que darão suporte às suas regras básicas. Para demonstrar que seus **TADs** funcionam de forma adequada, solicitaram que você produza um simulador de uma partida do jogo. 

Nesse simulador as cartas são distribuídas aleatoriamente entre de 2 a 4 jogadores virtuais. O simulador organiza de forma randômica os jogadores e indica um deles para iniciar a partida. Na sequencia todos os jogadores jogam uma vez, e o processo recomeça até que todas as cartas acabem. O controle das rodadas é feito pelo simulador. 

O simulador deve permitir que as jogadas sejam acompanhadas na tela. Deve ser possível ver as cartas de cada jogador, e a carta de cima do monte de cada jogador.  
	
As seguintes regras devem ser seguidas:

1. O baralho, um conjunto de cartas ordenado por naipe e por valor, deve ser gerado no início do jogo. Sua criação deve envolver um processo algoritmico e não uma inicialização por enumeração;
2. Um *Agrupamento de Cartas Embaralhadas (ACE)* deve ser definido no início de cada partida. O *ACE* deve ser gerado pelo sorteio aleatório de cartas do baralho;
3. O **mico** deve ser retirado do *ACE*, por sorteio, antes da distribuição para os jogadores ;
4. Tal como em um jogo real, a ordem das cartas do *ACE* deve mantida na distribuição das cartas aos jogadores; 
5. A distribuição das cartas entre os jogadores deve ser feita a partir da retirada de cartas do *ACE* e de forma alternada, ou seja, primeira retirada para o primeiro jogador, segunda para o segundo, terceira para o primeiro, quarta para o segundo, quinta para o primeiro, e assim sucessivamente, para o caso de apenas 2 jogadores;
6. O processo de retirada de uma carta da mão do outro jogador deve ser feita simulando a escolha da posição da carta pelo jogador da vez;
7. As cartas de cada jogador devem ser armazenadas de tal forma que a busca por um par em uma jogada seja a mais rápida possível;
8. O monte de cartas do jogador permite que apenas o ultimo par inserido fique visível aos outros jogadores.  

## Os Requisitos de implementação:

Seu simulador deverá ser codificado na linguagem Python [4], utilizando os conceitos de **Classes**, **Objetos** e **modularização**. 

Seu repositório deve conter um arquivo **README** com a documentação da solução adotada, que deve conter: 
1. Justificativa para o uso das estruturas de dados escolhidas;
2. Uma breve analise da complexidade dos principais métodos utilizados;
3. Instruções de como utilizar o programa, caso necessário. 
	
A submissão do código do seu projeto será feita exclusivamente pelo repositório individual disponibilizado no *GitHub Classroom*. 

Procure fazer `commits` e `pushs` regularmente, de modo a que seja possível acompanhar a evolução do seu código. 

Não serão aceitas submissões no *Google Classroom*, por e-mail ou qualquer outro meio eletrônico de envio. 

## A Avaliação:

Seu simulador será avaliado pelos critérios:
  
| Critério | Pontuação |
| :--- | :---: |
| 1. Documentação (README) [5] |  |
|  - Justificada da escolha dos TADs | 0,5 | 
|  - Analise da complexidade das operações | 0,5 | 
| 2. Geração do *ACE* | 1,5 |
| 3. Distribuição das cartas pelos jogadores | 1,5 |
| 4. Formação e armazenamento dos pares | 2,0 |
| 5. Simulação das jogadas | 2,0 |
| 6. Simulação completa | 2,0 |
| 7. Penalidades |  |
| - Atraso na entrega | 1,0 (p/dia) |
| - Código não seguindo boas práticas [4] | até 1,0 |
| - Uso correto do github (commits regulares) | até 0,5 |


## O Prazo e as Penalidades

Sua atividade deverá ser submetida até o dia 04/06 (domingo - 23:59).  

> Será aplicada a penalização de -1,0 pto por dia de atraso (verificado via data da ultima submissão no repositório)
> 
>> **A cooperação entre alunos é considerada salutar. No entanto, trabalhos com alto grau de similaridade serão tratados como “plágio”, o que resultará em avaliação 0 (zero) para todos os envolvidos.**. 

Qualquer dúvida adicional, evite problemas: não presuma nada, procure o professor para esclarecimentos.

## Referencias Bibliográficas:

[1] Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3a Edição, 2012.

[2]	Wikipedia. **Jogos de Cartas**. disponível em: https://pt.wikipedia.org/wiki/Jogos_de_cartas

[3]	WikiHow. **Como jogar mico em 12 passos**. disponível em: https://pt.wikihow.com/Jogar-Mico

[4] 	Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 

[5] 	**Markdown Guide**. Disponível em: https://www.markdownguide.org/basic-syntax/

[6]	**Boas Práticas de Programação**. Disponível em: https://liag.ft.unicamp.br/programacao2/boas-praticas-de-programacao/
