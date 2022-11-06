### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)

import sys
from threading import Thread

listaLinhas = [] #lista que contem sublistas com as linhas com ocorrencias da palavra em cada ficheiro

def pesquisa(ficheiro,palavra):
    """Recebe: um ficheiro e uma palavra. 
    Procura a palavra nesse ficheiro, imprime as linhas do ficheiro em que a palavra aparece.
    Returns: dicionario com numero de ocorrencias da palavra no ficheiro e o numero de linhas que contem a palavra
    """
    with open (ficheiro,"r") as f:
        global listaLinhas
        sublistaLinhas = []
        counter_ocorrencias = 0
        counter_linhas = 0
        lista_linhas = [] #indices das linhas em que aparece a palavra
        for linha in f: #le linhas do ficheiro
            for palavra_pesquisa in linha.split(): #le cada palavra da linha corrente
                if palavra_pesquisa == palavra: 
                    counter_ocorrencias += 1
                    if counter_linhas not in lista_linhas:    #para evitar que tenhamos duas linhas repetidas
                        lista_linhas.append(counter_linhas)
                        sublistaLinhas.append(linha)
            counter_linhas +=1
    
    listaLinhas.append(sublistaLinhas)

    return {
        "n_ocorrencias" : counter_ocorrencias,
        "n_linhas" : len(lista_linhas),
    }

def main(args):
    print('Programa: pgrepwc_threads.py')
    print('Argumentos: ',args)
    ficheiros = args[-1].split(",")
    palavra = args[-2]
    lista_dicts = [] #lista que contem dicionarios com numero de ocorrencias da palavra num certo ficheiro e numero de linhas em que a palavra ocorre
    listaT = [] #lista que guarda as threads
    if "-p" in args:
        n = int(args[int(args.index("-p")) + 1]) #sabemos que o número de threads a usar 
        for numero in range(n):
            listaT.append(Thread(target = pesquisa, args = (ficheiros[numero],palavra,)))
        for indice in range(len(listaT)):
            listaT[indice].start()
        for index in range(len(listaT)):
            listaT[index].join()
            lista_dicts.append(pesquisa(ficheiros[index], palavra))
            print(listaLinhas)
    else:
        for i in range(len(ficheiros)):
            lista_dicts.append(pesquisa(ficheiros[i], palavra))
    
    for indiceFicheiro in range(len(listaLinhas)):
        print(ficheiros[indiceFicheiro])
        for indiceLinha in range(len(listaLinhas[indiceFicheiro])):
            print(listaLinhas[indiceFicheiro][indiceLinha])

    totalOcorrencias = 0
    totalLinhas = 0

    for i in range(len(lista_dicts)):
            totalOcorrencias = totalOcorrencias + lista_dicts[i]["n_ocorrencias"]
    for j in range(len(lista_dicts)):
            totalLinhas = totalLinhas + lista_dicts[j]["n_linhas"]

    if "-c" in args and "-l" not in args:
        print("Número total de ocorrências: ", totalOcorrencias)
    elif "-c" not in args and "-l" in args:
        print("Número de linhas em que houve uma ou mais ocorrências: ", totalLinhas)
    elif "-c" in args and "-l" in args:
        print("Número total de ocorrências: ", totalOcorrencias)
        print("Número de linhas em que houve uma ou mais ocorrênciaa: ", totalLinhas)

if __name__ == "__main__":
    main(sys.argv[1:])
