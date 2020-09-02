import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random

df = pd.read_csv('data_normalized.csv') # Carregando o Dataset normalizado

# Separando as features das classificações
x = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])].values
y = df['Class']

# GERAR VÁRIOS INDIVÍDUOS
features = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])] # Retirando colunas do Dataset
features = np.array([features.columns.values]) # Salvando apenas os nomes das colunas para gerar os indivíduos
indBinary = np.array([random.randint(0, 1) for _ in range(52)]) # Gerando indivíduos de forma aleatória (Array de binários)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y,random_state=42) # Dividindo em conjunto de teste e treinamento

driver_classificator = DecisionTreeClassifier(random_state=42, max_depth=10) # Definindo parâmetros do modelo

def fitness(x_train, y_train, x_test, y_test, pos):
  
  driver_classificator.fit(x_train[:,pos], y_train)
  y_pred = driver_classificator.predict(x_test[:,pos])
  
  return accuracy_score(y_test, y_pred)

pos = [i==1 for i in indBinary] # Transformando o DNA do indivíduo em True e False
result_evolutivo = fitness(x_train, y_train, x_test, y_test, pos) 
print(result_evolutivo)



#driver_classificator.fit(x_train, y_train) # Treinando o modelo
#print(x_train)

#result = driver_classificator.predict(x_test) # Inserindo dados para o modelo classificar

# acc = accuracy_score(y_test, result) # Analisando a acurácia do modelo
#print(acc)















# import numpy as np
# import random
# import pandas as pd
# # Lendo o Dataset
# df = pd.read_csv('data_normalized.csv')

# # Retirando colunas do Dataset
# x = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])]

# # Salvando apenas os nomes das colunas para gerar os indivíduos
# x = np.array([x.columns.values])

# print(x)
# print(len(x))

# # Gerando indivíduos de forma aleatória (Array de binários)
# indBinary = np.array([random.randint(0, 1) for _ in range(52)])

# # Tranformando array de binários em bool
# indBool = np.array([i==1 for i in indBinary])
# #print(pos)

# # Transformando de bool para o nome das features
# individuo = (x[:,indBool])
# print(individuo)
