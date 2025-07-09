# Jogo do Mico no Terminal

![Imagem de capa do projeto](imgs/capa.png)

## Descrição

Este projeto implementa um simulador do jogo de baralho **Mico**, utilizando os conceitos de **Tipos Abstratos de Dados (TAD) Lineares** como **Listas Encadeadas**, **Pilhas** e **Filas**. O objetivo é aplicar esses conceitos em um problema prático de forma eficiente, simulando as regras do jogo e a interação entre jogadores virtuais.

## Estruturas de Dados Utilizadas

Para a implementação do simulador do jogo de Mico, foram escolhidas as seguintes estruturas de dados, levando em conta a eficiência e as características necessárias para cada componente do jogo:

### 🃏 Pilhas para o monte de cartas

Cada jogador possui um monte onde são colocados os pares de cartas formados durante o jogo. Utilizamos **pilhas** para representar esse monte, pois:

- Permitem que apenas o **último par inserido fique visível**, conforme a regra do jogo.
- A inserção e remoção no topo da pilha são operações rápidas, com complexidade **O(1)**.

### ✋ Lista simplesmente encadeada para as cartas na mão do jogador

A mão de cartas de cada jogador foi representada por uma **lista simplesmente encadeada**, pois:

- Permite **inserção e remoção dinâmicas** à medida que o jogo avança.
- Facilita o **percorrer das cartas** para buscar pares ou selecionar cartas para serem retiradas por outro jogador.

![Imagem das cartas do jogador](assets/Cartas.png)

### 🔁 Lista circular para a ordem dos jogadores

Para controlar a sequência das jogadas e garantir a rotação cíclica entre os jogadores, utilizamos uma **lista circular**, que:

- Permite avançar de um jogador ao próximo de forma contínua.
- **Simula a ordem real do jogo**, voltando ao primeiro jogador após o último sem a necessidade de reinicialização da lista.

## Como Utilizar

1. Clone este repositório.
2. Execute o programa principal `main.py` (ou arquivo equivalente).
3. O simulador iniciará uma partida com 2 a 4 jogadores virtuais.
4. As cartas serão distribuídas, e o jogo rodará automaticamente exibindo as jogadas e o estado das mãos e montes.
5. Acompanhe a saída no terminal para ver a evolução da partida e identificar o jogador perdedor que ficará com o "mico".

![Imagem do jogo](assets/Distribui.png)

## Referências

- [Algoritmos – Teoria e Prática, Cormen et al.](https://pt.wikipedia.org/wiki/Algoritmos)
- [Jogos de Cartas - Wikipedia](https://pt.wikipedia.org/wiki/Jogos_de_cartas)
- [Como jogar Mico - WikiHow](https://pt.wikihow.com/Jogar-Mico)
- Canning, J., Broder, A., Lafore, R. *Data Structures & Algorithms in Python*. Addison-Wesley, 2022.
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Boas Práticas de Programação - Unicamp](https://liag.ft.unicamp.br/programacao2/boas-praticas-de-programacao/)

---

*Este projeto foi desenvolvido em 2022 como parte da avaliação da disciplina de Estruturas de Dados da UFBA.*
