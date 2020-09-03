import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

def fitness(populacao): # Função que treina o modelo e avalia para cada indivíduo
  acuracias = []
  df = pd.read_csv('data_normalized.csv') # Carregando o Dataset normalizado
  x = df[df.columns.difference(['Class', 'Time(s)', 'PathOrder'])].values
  y = df['Class']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y,random_state=42) # Dividindo em conjunto de teste e treinamento
  driver_classificator = DecisionTreeClassifier(random_state=42, max_depth=10) # Definindo parâmetros do modelo
  for ind in populacao: 
    driver_classificator.fit(x_train[:,ind], y_train)
    y_pred = driver_classificator.predict(x_test[:,ind])
    acuracias.append(accuracy_score(y_test, y_pred))
  return acuracias
