### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)


import multiprocessing
import sys

#tenho que declarar word e ficheiros aqui p poder usar nos shared arrays
for i in range(len(sys.argv[1:])):
    if "-p" in sys.argv[1:]:
        nProcessos=int(sys.argv[1:][int(sys.argv[1:].index("-p")) + 1]) #sabemos que o num processos vem a seguir ao -p (na lista args), entao vamos busca-lo usando args[indice a seguir a -p]
        #aqui porque ja tenho um numero e o argumento antes da palavra nao leva um "-" tenho que mudar os indices das pos da word e ficheiros
        word = sys.argv[1:][sys.argv[1:].index(str(nProcessos)) + 1]
        ficheiros = sys.argv[1:][sys.argv[1:].index(word) +1 :]
    else:
        if sys.argv[1:][i][0] != "-":
            word = sys.argv[1:] [i]
            ficheiros = sys.argv[1:] [i+1:]
            break #tenho que dar o break senao ele continua o for e vai atualizando o word e os ficheiros para a string que aparece a seguir

   
shared_array_nocorrencias = multiprocessing.Array("i",len(ficheiros)) #lista c ocorrencias da palavra.
#continuacao da linha acima: indice 0 = ocorrencias da palavra no ficheiro na posicao 0 (em ficheiros)
shared_array_nlinhas = multiprocessing.Array("i",len(ficheiros)) #lista c n_linhas em que a palavra aparece no ficheiro
def pesquisa(indice_ficheiro,ficheiro,palavra,queue,array_ocorrencias,array_linhas): #tenho q por os arrays aqui pq os filhos n conseguem ler os arrays criados acima
    with open (ficheiro,"r") as f:
        counter_ocorrencias = 0
        counter_linhas = 0
        lista_linhas = [] #indices das linhas em que aparece a palavra
        for linha in f: #le linhas do ficheiro
            for palavra_pesquisa in linha.split(): #le cada palavra da linha corrente
                if palavra_pesquisa == palavra: 
                    counter_ocorrencias += 1
                    if counter_linhas not in lista_linhas:    #para evitar que tenhamos duas linhas repetidas
                        lista_linhas.append(counter_linhas)
                        queue.put(linha)
            counter_linhas +=1
    array_ocorrencias[indice_ficheiro] = counter_ocorrencias
    array_linhas[indice_ficheiro] = len(lista_linhas)


def main(args):
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ', args)
    if "-p" not in args:
        for i in range(len(ficheiros)):
            q = multiprocessing.Queue()
            pesquisa (i,ficheiros[i],word,q,shared_array_nocorrencias,shared_array_nlinhas)
            #print do nome do ficheiro
            print (f'NOME DO FICHEIRO: {ficheiros[i]}')
            #imprime linhas que estao na queue ate a queue estar vazia
            while q.empty() == False:
                print (q.get())
            

    elif "-p" in args:
        
        if nProcessos>len(ficheiros) or nProcessos==len(ficheiros):
            lista_processos = []
            lista_queues = []
            for i in range(len(ficheiros)): #criamos processos. para cada ficheiro criamos um processo
                q = multiprocessing.Queue()
                lista_queues.append(q)
                processo = multiprocessing.Process(target = pesquisa, args = (i,ficheiros[i],word,lista_queues[i],shared_array_nocorrencias,shared_array_nlinhas) )
                processo.start()
                lista_processos.append(processo)  
            for processo in lista_processos:
                processo.join()

            for i in range(len(lista_queues)):
                print (f'NOME DO FICHEIRO: {ficheiros[i]}')
                #imprime linhas que estao na queue ate a queue estar vazia
                while lista_queues[i].empty() == False:
                    print (lista_queues[i].get())
    
        elif nProcessos<len(ficheiros):
            #distribute the files thru processes. create sublists. 1st process runs 1st sublist
            for i in nProcessos:

    ocorrencias_total = 0
    linhas_total = 0
    for i in range(len(ficheiros)): 
        ocorrencias_total = ocorrencias_total + shared_array_nocorrencias[i]
        linhas_total = linhas_total + shared_array_nlinhas[i]
        

    #check se -c (n total de ocorrencias) e -l (n total de linhas) estao presentes e da print se sim
    if "-c" in args:
        print (f'\nNúmero total de ocorrências: {ocorrencias_total}')
    if "-l" in args:
        print (f'Número de linhas em que houve uma ou mais ocorrências: {linhas_total} \n')


if __name__ == "__main__":
    main(sys.argv[1:])
