import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random


def createIndividual():
  populacao = []
  for i in range(5):
    dna = np.array([random.choice([True, False]) for _ in range(52)])
    populacao.append(dna)
    dna = []
  return populacao




# features = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])] # Retirando colunas do Dataset
# features = np.array([features.columns.values]) # Salvando apenas os nomes das colunas para gerar os indivíduos

# columns=['Individual', 'Accuracy', 'Number_of_Features_used', 'Features_used',  'Array_bool']
# results = pd.DataFrame(columns=columns)