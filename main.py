import pandas as pd
from geopy.distance import geodesic
import matplotlib.pyplot as plt


#Cria uma grafo usando dicionarios a partir da base, respeitando o numero de vertices a ser analisado e de onde ira iniciar
#além disso, destribui os pesos levando em consideração a distancia entre os vertices
#estou usando a biblioteca geopy.distance que utiliza a formula de haversine como base 
def criarGrafo(base, numVertices, inicio):
    G = {}
    #Usando o dicionario criado, primeiro é percorrido do inicio ate o numero de vertices indicados
    #Entoa pra cada vertice é inserido no dicionario usando o indice e posicao(latitude e longitude)
    for i in range(inicio, inicio + numVertices):
        G[i] = {'pos': (base.loc[i, 'latitude'], base.loc[i, 'longitude']), 'arestas': {}}

    #percorre todos os vertices para identificar quais são os adjacentes, faz o calculo da distancia entre eles e 
    #os adiciona como arestas com a posicao e o peso correspondente
    for i in range(inicio, inicio + numVertices):
        for j in range(i + 1, inicio + numVertices):
            coord1 = G[i]['pos']
            coord2 = G[j]['pos']
            distancia = geodesic(coord1, coord2).km
            G[i]['arestas'][j] = {'pos': coord2, 'peso': distancia}
            G[j]['arestas'][i] = {'pos': coord1, 'peso': distancia}

    return G

#Implementacao do algoritmo de prim para calcular a arvore geradora mínima
#leva em consideracao o inicio, ou seja, de onde quero começar a percorrer e montar a arvore
#faz uso de tres dicionarios para ir verificando as informacoes sobre os vertices, sao eles: pai, custo e visitado
def prim(G, inicio):
    #custos iniciados como infinito, menos o de inicio que é setado abaixo
    custo = {v: float('inf') for v in G}
    #todos os pais sao iniciados como none, e depois serao setados
    pai = {v: None for v in G}
    #também todos sao marcados como false para visitados
    visitado = {v: False for v in G}

    #o vertice de inicio recebe o custo zero, pra iniciarmos por ele
    custo[inicio] = 0

    #For para iterar o numero de vezes que for o tamanho do grafo
    for _ in range(len(G)):
        #Verifica  o vertice não visitado que tem menor custo
        #percorre e filtra os vertices nao visitados, como esta sendo usado uma funcao lambda para extrair
        #o custo de cada vertice, usando a funcao de minimo por fora, teremos o vertice de menor custo dentro todos nao visitados
        u = min((v for v in G if not visitado[v]), key=lambda x: custo[x])

        #O vertice então é marcado como visitado
        visitado[u] = True

        #Atualiza o custo dos pais dos vertices adjacentes
        #percorre os vertices adjacentes, ficando com o indice do vetice adjacente e as informacoes
        #pertinentes a ele
        for v, dado in G[u]['arestas'].items():
            #vai verificar se o vertice não foi visitado e se o custo é menor que o de v
            if not visitado[v] and dado['peso'] < custo[v]:
                #caso seja, vai atualizar o pai do vertice v para ser u, fazendo o funcionameento
                #importante pra que o algoritmo de prim funcione e comece a criar a arvore minima com os menores custos
                custo[v] = dado['peso']
                pai[v] = u

    #Cria a arvore minima
    arvoreMinima = {v: {'arestas': {}} for v in G}

    for v in G:
        u = pai[v]
        #verifica se ha um pai, se não ouver, é um vertice inicial
        if u is not None:
            #adiciona na arvore minima as entradas que correspondem  as arestas entre "u" e "v" e "v" e "u"
            arvoreMinima[u]['arestas'][v] = {'pos': G[v]['pos'], 'peso': custo[v]}
            arvoreMinima[v]['arestas'][u] = {'pos': G[u]['pos'], 'peso': custo[v]}
    #Ou seja, essa parte cria a representacao da arvore minima que sera retornada
    return arvoreMinima

def geraGraficos(G, posicoes, titulo):
    plt.figure(figsize=(10, 10))
    
    #faz a iteracao sobre todos o vertices do grafo, pegando seu indice e suas informacoes
    for u, dado in G.items():
        #cria os pontos de dispersao a partir das posicoes, com o tamanho setado, a cor do no e  sua borda
        plt.scatter(posicoes[u][0], posicoes[u][1], s=300, facecolors='blue', edgecolors='black')
        #adiciona a informacao do no, que é o seu indice, sentando também fote, cor e posiconamento no no, que é centralizado
        plt.text(posicoes[u][0], posicoes[u][1], str(u), fontsize=12, color='white', ha='center', va='center')

        #como ja tratamos os vertices, agora vamos percorrer todas as arestas e pegar suas posicoes e peso
        for v, dadosExt in dado['arestas'].items():
            #plota a linha ente os vertices de acordo com a posicao, na cor preta
            plt.plot([posicoes[u][0], dadosExt['pos'][0]], [posicoes[u][1], dadosExt['pos'][1]], 'black')
            #adiciona as informacoes nas arestas, que sera o peso colocado em km, seta-se também a fonte e a centralizacao
            plt.text((posicoes[u][0] + dadosExt['pos'][0]) / 2, (posicoes[u][1] + dadosExt['pos'][1]) / 2,
                     f"{dadosExt['peso']:.2f} km", fontsize=10, ha='center', va='center')

    #plata o titulo do grafico, passado no main porque vamos ter um plot antes e depois de usar o prim
    plt.title(titulo)
    #Desativa a exibicao dos eixos, pra que fique mais limpo trazendo só as arestas, os vertices e suas informacoes
    plt.axis('off')
    plt.show()

#vamos chamar todas as funcoes, setar a base a ser utilizada e plotar os graficos
def main():
    #ler o arquivo .csv usando o pandas
    arquivo = "e6e4ac72-ff15-4c5a-b149-a1943386c031.csv"
    base = pd.read_csv(arquivo)

    #solicita o vertice que se quer iniciar e quantos quer analisar
    inicio = int(input("Digite o vértice de início: "))
    numVertices = int(input("Digite o número de vértices a serem analisados: "))

    #cria o grafo com base nas informacoes passadas
    G = criarGrafo(base, numVertices, inicio)

    #mostrar o gráfico original, mapeando todas as chaves do grafo G usando o G.keys()
    #Logo depois é passado pra criacao do grafico o grafo, a posicao e o título
    posOriginal = {i: G[i]['pos'] for i in G.keys()}
    geraGraficos(G, posOriginal, f"Grafo Original - {numVertices} Vértices")

    # Executar o algoritmo de prim pra agora gerar a arvore minima
    arvoreMinima = prim(G, inicio)

    # Mostrar o resultado apos o prim, armazenado as posicoes no dicionario criado 
    posArvoreMinima = {}
    #pega as informacoes da arvore minima gerada pelo prim
    #vai pegar as informacoes de adjacencias pra entao gerar o gratico
    for u, dado in arvoreMinima.items():
        for v, dadosExt in dado['arestas'].items():
            posArvoreMinima[u] = G[u]['pos']
            posArvoreMinima[v] = dadosExt['pos']
    #grafico gerado apos a passagem pelo algoritmo de prim, passando a arvore minima(Grafo final)
    #as posicoes e o titulo        
    geraGraficos(arvoreMinima, posArvoreMinima, f"Árvore Geradora Mínima (Prim) - {numVertices} Vértices")

if __name__ == "__main__":
    main()
