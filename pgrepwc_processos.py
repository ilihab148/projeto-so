### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)

import multiprocessing 
import sys


def pesquisa(ficheiro,palavra):
    """Recebe: um ficheiro e uma palavra. 
    Procura a palavra nesse ficheiro, imprime as linhas do ficheiro em que a palavra aparece.
    Returns: dicionario com numero de ocorrencias da palavra no ficheiro e o numero de linhas que contem a palavra
    """
    with open (ficheiro,"r") as f:
        counter_ocorrencias = 0
        counter_linhas = 0
        lista_linhas = [] #indices das linhas em que aparece a palavra
        for linha in f: #le linhas do ficheiro
            for palavra_pesquisa in linha.split(): #le cada palavra da linha corrente
                if palavra_pesquisa == palavra: 
                    counter_ocorrencias += 1
                    if counter_linhas not in lista_linhas:    #para evitar que tenhamos duas linhas repetidas
                        print (linha) #print das linhas em que a palavra aparece
                        lista_linhas.append(counter_linhas)
            counter_linhas +=1
    
    return {
        "n_ocorrencias" : counter_ocorrencias,
        "n_linhas" : len(lista_linhas),
    }

def main(args):
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ', args)
    ficheiros = args[-1].split(",")
    word = args[-2]
    lista_dicts = [] #lista que contem dicionarios com numero de ocorrencias da palavra num certo ficheiro e numero de linhas em que a palavra ocorre
    if "-p" not in args:
        for ficheiro in ficheiros:
            lista_dicts.append(pesquisa (ficheiro,word))
    if "-p" in args:
        for i in range(len(ficheiros)): #criamos processos. para cada ficheiro criamos um processo
            process = multiprocessing.Process(target = pesquisa, args = (ficheiros[i],word) )
            print (process)



if __name__ == "__main__":
    main(sys.argv[1:])

   
#DAR LOGO PRINT DAS LINHAS E N OCORRENCIAS EM PESQUISA PQ SE FIZER COM PROCESSOS ELE CORRE ME LOGO E NAO FACO MAIS LOOPS NO MAIN
#Imprimir linhas
#função que destribui trabalho entre processos de forma igual 
#função que manda trabalhar os processos 
#função que calcula todas as ocorrencias de todos os processos 
#para teste:   ./pgrepwc  -p "documento" "teste.txt,teste2.txt"
