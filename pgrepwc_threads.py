### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)

import sys
from threading import Thread

listaLinhas = [] #lista que contem sublistas com as linhas com ocorrencias da palavra em cada ficheiro
lista_dicts = [] #lista que contem dicionarios com numero de ocorrencias da palavra num certo ficheiro e numero de linhas em que a palavra ocorre

def pesquisa(listaFicheiros,palavra):
    for ficheiro in listaFicheiros: #corre a lista de ficheiros dos parametros
        with open (ficheiro,"r") as f:
            sublistaLinhas = [] #guarda uma sublista das linhas em que ha uma ou mais occrencias de uma palavra (uma sublista por ficheiro)
            dicts = {} #dicionario com numero de ocorrencias e numero de linhas
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
            dicts = {
            "n_ocorrencias" : counter_ocorrencias,
            "n_linhas" : len(lista_linhas),
            }
            lista_dicts.append(dicts)
        
def main(args):
    print('Programa: pgrepwc_threads.py')
    print('Argumentos: ',args)

    for indiceComando in range(len(sys.argv)):
        if sys.argv[indiceComando] == "-t":
            palavra = sys.argv[indiceComando + 1]
            indiceComecaFicheiros = indiceComando + 2
            break
    ficheiros = [sys.argv[f] for f in range(indiceComecaFicheiros, len(sys.argv))] #lista com os ficheiros dos argumentos
    listaT = [] #lista que guarda as threads
    listaFicheirosIgual = [ficheiros[i:i + 1] for i in range(0, len(ficheiros), 1)] #separa os ficheiros em sublistas

    if "-p" in args:
        n = int(args[int(args.index("-p")) + 1]) #sabemos o número de threads a usar 
        if n >= len(ficheiros):
            n = len(ficheiros)
            for numero in range(len(listaFicheirosIgual)):
                listaT.append(Thread(target = pesquisa, args = (listaFicheirosIgual[numero],palavra)))
                listaT[numero].start()
            for index in range(len(listaT)):
                listaT[index].join()  
        else:
            listaFicheiroDividida = [ficheiros[i:i + n] for i in range(0, len(ficheiros), n)] #divide os ficheiros pelas threads
            for num in range(len(listaFicheiroDividida)):
                listaT.append(Thread(target = pesquisa, args = (listaFicheiroDividida[num],palavra)))
                listaT[num].start()
            for indx in range(len(listaT)):
                listaT[indx].join()
    else:
        for i in range(len(ficheiros)):
            pesquisa(listaFicheirosIgual[i], palavra)
    
    for indiceFicheiro in range(len(listaLinhas)):
        print("NOME DO FICHEIRO: " + ficheiros[indiceFicheiro])
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
        print("Número de linhas em que houve uma ou mais ocorrêcias: ", totalLinhas)
    elif "-c" in args and "-l" in args:
        print("Número total de ocorrências: ", totalOcorrencias)
        print("Número de linhas em que houve uma ou mais ocorrências: ", totalLinhas)

if __name__ == "__main__":
    main(sys.argv[1:])
