from Population import createIndividual
import random 

populacao = createIndividual()


parent1 = random.choice(populacao)
parent2 = random.choice(populacao)

mutation_prob = 0.2
crossover_prob = 1 - 0.2

r = random.randint(0,1)

n_permutacoes = 40
print(parent1)
for n in range(n_permutacoes):
  if (r < mutation_prob): #gerar filho com mutacao
    dna = random.choice(range(len(parent1)))
    if (parent1[dna]==True):
      parent1[dna]=False
    else:
      parent1[dna]=True
  else: # gerar filho com crossover
    print('Crossover')

print(parent1)


#print(parent1)
#print(parent2)
#for p in populacao:
#  populacao[1]
#  populacao[2]
