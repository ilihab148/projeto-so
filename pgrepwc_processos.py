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
        ocorrencias_total = 0
        linhas_total = 0
        for i in range(len(lista_dicts)):
            ocorrencias_total = ocorrencias_total + lista_dicts[i]["n_ocorrencias"]
            linhas_total = linhas_total + lista_dicts[i]["n_linhas"]
        
        #check se -c (n total de ocorrencias) e -l (n total de linhas) estao presentes e da print se sim
        if "-c" in args:
            print (f'ocorrências da palavra: {ocorrencias_total}')
        if "-l" in args:
            print (f'número de linhas em que a palavra aparece: {linhas_total}')
        
    elif "-p" in args:
        numeros=[x for x in args if type(x)==int] #faz uma lista com os numeros dados no argumenti
        nProcessos=numeros[0]   #Assim é possivel descobrir o numero associado ao -p
        if nProcessos>len(ficheiros) or nProcessos==len(ficheiros):
            for i in range(len(ficheiros)): #criamos processos. para cada ficheiro criamos um processo
                processo = multiprocessing.Process(target = pesquisa, args = (ficheiros[i],word) )
                processo.start()
                
             
             
        elif nProcessos<len(ficheiros):
    
        
        

if __name__ == "__main__":
    main(sys.argv[1:])

    

#função que distribui trabalho entre processos de forma igual 
#função que manda trabalhar os processos 
#função que calcula todas as ocorrencias de todos os processos 
#para testar: 
#uma solucao para os processos pode ser uma versao do pesquisa mas em vez de retornar o dicionarios, escreve tudo num dicionario global cujos dados podem ser usados mais tarde.isto porque os processos nao retornam nada
#criamos um dicionario global e vamos guardando as nossas variaveis e listas e quando a funcao correr outra vez comeca as vars locais do zero
#possible solution: https://stackoverflow.com/questions/10415028/how-can-i-recover-the-return-value-of-a-function-passed-to-multiprocessing-proce
#ver codigo da catarina para check se ha um numero nos args
 
        #lista_processos = []
        #for i in range(len(ficheiros)): #criamos processos. para cada ficheiro criamos um processo
           # processo = multiprocessing.Process(target = pesquisa, args = (ficheiros[i],word) )
            #processo.start()
        #for processo in lista_processos:
            #processo.join() #se colocassemos o join no loop acima, ele so continuava a correr o loop quando o processo corrente acabasse