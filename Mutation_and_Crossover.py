from Population import createIndividual
import random 

populacao = createIndividual()


parent1 = random.choice(populacao)
parent2 = random.choice(populacao)

mutation_prob = 0.2
crossover_prob = 1 - 0.2

r = random.randint(0,1)
r = 0.3
n_permutacoes = 1
print('P1 Original: ', parent1, '\n')
print('P2 Original: ', parent2, '\n\n')

if (r < mutation_prob):
  print('----------- Mutation ----------')
else:
  print('----------- Crossover -----------')

for n in range(n_permutacoes):
  if (r < mutation_prob): #gerar filho com mutacao
    dna = random.choice(range(len(parent1)))
    if (parent1[dna]==True):
      parent1[dna]=False
    else:
      parent1[dna]=True
    print('Mutation: ', parent1)
  else: # gerar filho com crossover
    point = random.randint(0,51)
    print('Crossover Point: ', point)
    kid1=parent2[:1]+parent1[1:]
    kid2=parent1[:1]+parent2[1:]
    
    print('Kid1: ', kid1)
    print('Kid2: ', kid2)


#print(parent1)
#print(parent2)
#for p in populacao:
#  populacao[1]
#  populacao[2]
