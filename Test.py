
# saida = []
# for _ in range(x):
#     saida.append(random.choice(range(2)))
# print(saida)\

import random
 
x = 50

saida = [random.randint(0, 1) for _ in range(x)]
print(saida)