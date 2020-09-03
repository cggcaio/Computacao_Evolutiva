from Evaluation import fitness # Importando a função que treina o modelo e avalia os individuos
from Population import createIndividual # Importando a função que cria a população

populacao = createIndividual()

result = fitness(populacao)
