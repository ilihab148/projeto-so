### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)

import sys


def pesquisa(ficheiro,palavra):
    with open (ficheiro,"r") as f:
        counter_ocorrencias = 0
        counter_linhas = 0
        linhas_out = [] #indices das linhas em que aparece a palavra
        for linha in f.readlines(): #le linhas do ficheiro
            for palavra_pesquisa in linha.split(): #le cada palavra da linha corrente
                if palavra_pesquisa == palavra: 
                    counter_ocorrencias += 1
                    if counter_linhas not in linhas_out:    #para evitar que tenhamos duas linhas repetidas
                        print(counter_linhas)
                        linhas_out.append(counter_linhas)
            counter_linhas +=1
    
    return (counter_ocorrencias,linhas_out)



def main(args):
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ', args)
    ficheiros = args[-1].split(",")
    word = args[-2]
    lista_tuplos = [] #contem tuplos cuja pos 0 e o n_ocorrencias da palavra no ficheiro e pos 1 e uma lista de linhas em que aparece a palavra
    #ocorrencias_palavra = [ocorrencias_ficheiro1,ocorrencias_ficheiro2,etc]
    for ficheiro in ficheiros:
       lista_tuplos.append(pesquisa (ficheiro,word))
    print (lista_tuplos)




if __name__ == "__main__":
    main(sys.argv[1:])

   
#DAR LOGO PRINT DAS LINHAS E N OCORRENCIAS EM PESQUISA PQ SE FIZER COM PROCESSOS ELE CORRE ME LOGO E NAO FACO MAIS LOOPS NO MAIN
#Imprimir linhas
#função que destribui trabalho entre processos de forma igual 
#função que manda trabalhar os processos 
#função que calcula todas as ocorrencias de todos os processos 
