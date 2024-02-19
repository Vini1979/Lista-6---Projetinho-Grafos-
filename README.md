# Árvore Geradora Mínima (Prim) - Análise Bike PE

Este projeto implementa o algoritmo de Prim para encontrar uma Árvore Geradora Mínima em um grafo ponderado, onde os pesos são calculados usando como base a distancia geoespacial entre os vértices. Será analisada a base: http://dados.recife.pe.gov.br/dataset/ciclovias-ciclofaixas-estacoes-de-aluguel-de-bikes-e-rotas/resource/e6e4ac72-ff15-4c5a-b149-a1943386c031

Disponibilizada pela prefeitura do Recife

## Funcionalidades

- **Leitura de Dados:** O programa lê dados de localização (latitude e longitude) de um arquivo CSV.
- **Criação do Grafo:** Um grafo é criado com base nos dados lidos, considerando distâncias geoespaciais como pesos.
- **Prim:** O algoritmo de Prim é aplicado para encontrar a árvore geradora mínima a partir de um vértice inicial, considerando um vertice de inicio escolhido e um número específico de vértices
- **Plotagem Gráfica** Plotagem de graficos representando a forma original desse grafo e a árvore geradora mínima

## Pré-requisitos

- Python 3.x
- Bibliotecas: pandas, matplotlib, geopy

## Como Usar

1. Clone este repositório:
2. Certifique-se de colocar o arquivo na pasta indicada(raiz do programa) com o nome setado no programa para que a leitura seja feita
3. Ao gerar as entradas, escolha como inicio um número de 1 à 91, e para quantidade a ser análisada, um número superior ao inicio e que componha até o 91(número de vértices da base)

Clone:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git](https://github.com/Vini1979/Lista-6---Projetinho-Grafos-.git)https://github.com/Vini1979/Lista-6---Projetinho-Grafos-.git 
