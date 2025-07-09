# Jogo do Mico

# OBS: ABRIR O JOGO COM O TERMINAL EM TELA CHEIA

## Justificativa e explicação

Para a elaboração do jogo do mico, foram utilizados três tipos de TADs: pilha, lista simplesmente encadeada e lista circular.

No módulo "carta.py", encontra-se a classe "Carta", que representa um nó. Essa classe armazena o "naipe" e o "dado" da carta, e possui um ponteiro para o próximo elemento da lista.

No módulo "baralho.py", a classe "Baralho" herda os métodos de uma pilha e é responsável por organizar o baralho inicial do jogo e a pilha de pares de cada jogador. Essa estrutura de dados mostrou-se eficiente, pois, assim como em uma pilha, a última carta a entrar no baralho é a primeira a sair. Na classe "Baralho", os elementos são removidos ou inseridos no final da pilha, exceto no método "pop.mico()", onde um elemento de posição aleatória é removido, exigindo o uso de herança.

No módulo "jogador.py", a classe "Jogador" é uma lista simplesmente encadeada. A escolha desse TAD foi feita devido à sua estrutura flexível, que permite alocação dinâmica. Ao contrário das pilhas e filas, é possível inserir ou remover elementos em qualquer posição. O uso desse TAD foi necessário para remover as cartas da mão de cada jogador, com base na escolha da posição, conforme requerido pelo problema.

No módulo "Ordem", a escolha de uma lista circular para organizar os jogadores foi feita pela mesma necessidade de inserção e remoção de elementos em qualquer posição. No entanto, para garantir a continuidade das jogadas, foi necessário que, ao terminar a vez do último jogador, a ordem voltasse para o primeiro jogador, assim como em uma lista circular em que o fim aponta para o início.

## Análise da complexidade

A complexidade de inserção utilizada nas listas encadeadas e na pilha é sempre constante O(1), pois é realizada sem a necessidade de percorrer os elementos de um vetor ou lista, sendo independente do seu tamanho.

No caso da lista simplesmente encadeada 'Jogador', a remoção por posição (método 'perde()') possui complexidade linear O(n). O pior caso ocorre quando a posição escolhida é a última da lista, resultando em complexidade O(n). O melhor caso é quando a remoção é feita da primeira posição, tendo complexidade O(1). O caso médio é O(n). Da mesma forma, a remoção na lista circular 'Ordem' (método 'player_left()') tem a mesma complexidade e depende da posição ocupada pelo jogador a ser removido.

O método 'abaixa_par()' da classe 'Jogador' também possui a mesma complexidade dos métodos descritos anteriormente. Ele funciona procurando a primeira carta que seja igual à carta da posição inicial. No pior caso, com complexidade O(n), ocorre quando a última carta inserida (início da lista) não tem um par na mão do jogador, ou quando o par está localizado na última posição. O melhor caso, com complexidade O(1), ocorre quando a carta na segunda posição da lista é o par da carta inicial. O caso médio é O(n).

Por outro lado, o método 'abaixa_pares()', também da classe 'Jogador', funciona de forma semelhante ao último método descrito, porém repete o processo para cada uma das cartas na mão do jogador. Portanto, sua complexidade é O(n^2) no pior caso, quando não existem pares na mão do jogador, e O(n) no melhor caso, quando os pares estão armazenados lado a lado.

