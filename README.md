# Computacao Evolutiva
 
Repositório criado para a disciplina BCC461 - Computação Evolutiva

O objetivo do trabalho é criar um Algoritmo Genético capaz de otimizar a quantidade de Features necessárias para classificar um motorista. 

## Estrutura do Repositório
### Principal
No arquivo [Main.py](https://github.com/cggcaio/Computacao_Evolutiva/blob/master/Main.py) são chamadas todas as funções do projeto. 
### Tratamento do Dataset
No arquivo [Data_Treatment.py](https://github.com/cggcaio/Computacao_Evolutiva/blob/master/Data_Treatment.py) é normalizado o Dataset e gerado um arquivo .csv.
### População
[Population.py](https://github.com/cggcaio/Computacao_Evolutiva/blob/master/Population.py): Escolher o tamanho e gerar a população. 
### Gerando o modelo de classificação e primeiros indivíduos da população
No arquivo [Soluction_Features_Class.py](https://github.com/cggcaio/Computacao_Evolutiva/blob/master/Soluction_Features_Class.py) é desenvolvido o modelo de regressão (Decision Tree) e são gerados os primeiros indíviduos que são testados no modelo de classificação.
