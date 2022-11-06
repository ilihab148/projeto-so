### Grupo: SO-TI-13
### Aluno 1: Catarina Alves (fc58667)
### Aluno 2: Eduardo Viana (fc58776)
### Aluno 3: Iliyan Habibo (fc58626)

### Exemplos de comandos para executar o pgrepwc:
1) ./pgrepwc -c -l palavra ficheiro1.txt ficheiro2.txt    
2) ./pgrepwc -c -l -p 3 palavra ficheiro1.txt ficheiro2.txt ficheiro3.txt ficheiro4.txt   
3) ./pgrepwc -c -l -p 3 -t palavra ficheiro1.txt ficheiro2.txt ficheiro3.txt     

### Limitações da implementação:
- não foi implementado o programa com o parâmetro "-e" (caso especial de paralelização)
- no ficheiro das threads, por vezes, o output aparece fora de ordem

### Abordagem para a divisão dos ficheiros:
- lista por compreensão (ficheiros_sublistas = [ficheiros[i:i + nProcessos] for i in range(0, len(ficheiros), nProcessos)])
ficheiros- lista com os nomes dos ficheiros


### Outras informações pertinentes:
- ...
- ...
